import json
import re

import requests

from src.products.v1.domain.product import Product
from src.products.v1.serializers.product_serializers import ProductBaseSchema
from src.shared.helper import find_between
from src.shared.response_object import ResponseSuccess, ResponseFailure
from src.shared.use_case import UseCase


class ProductCrawl(object):

    @staticmethod
    def get_product(product):
        r = requests.get(product.url)
        html = r.text
        string = find_between(html, '<script type="application/ld+json" class="y-rich-snippet-script">', '</script>')
        string = re.sub(r"[\s+]", ' ', string)
        if string:
            data = json.loads(string)
            offers = data.get('offers', {})

            product.sku = data.get('sku')
            product.name = data.get('name')
            product.brand = data.get('brand')
            product.image = data.get('image')
            product.description = data.get('description')
            product.width = data.get('width')
            product.height = data.get('height')
            product.weight = data.get('weight')
            product.price = offers.get('price')
            product.price_currency = offers.get('priceCurrency')


class ProductListUseCase(UseCase):

    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        pages = self.repo.get_all(request_objects)
        total = self.repo.get_total(request_objects)
        page_schema = ProductBaseSchema()
        serialize = page_schema.dump(pages, many=True)
        response = {
            'meta': {
                'totalData': total,
            },
            'data': serialize.data
        }
        return ResponseSuccess(response)


class ProductCreateUseCase(UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_objects):
        check = self.repo.get_by_url(request_objects.url)
        if check:
            return ResponseFailure.build_parameters_error("URL already exist!")

        product = Product(
            id=None,
            url=request_objects.url,
        )

        ProductCrawl.get_product(product)

        last_id = self.repo.create(product=product)

        return ResponseSuccess({'id': last_id})


class ProductDetailUseCase(UseCase):
    def __init__(self, repo):
        self.repo = repo

    def process_request(self, request_object):
        product = self.repo.get_by_id(id=request_object.id)
        if product is None:
            return ResponseFailure.build_data_not_found_error(
                'Data dengan id: {} tidak ditemukan'.format(request_object.id))

        if request_object.crawl:
            # Insert history price
            data = {
                'product_id': product.id,
                'price': product.price,
                'price_currency': product.price_currency,
                'created_at': product.created_at,
                'updated_at': product.updated_at
            }
            self.repo.create_price_history(data)

            ProductCrawl.get_product(product)

        product.price_history = self.repo.get_price_history(product.id)

        serialize = ProductBaseSchema().dump(product).data
        return ResponseSuccess(serialize)
