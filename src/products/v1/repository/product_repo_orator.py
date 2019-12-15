"""
Repository Product
"""

from src.shared import helper
from src.products.v1.domain.product import Product, PriceHistory
from src.products.v1.repository.product_repo import ProductRepository


class ProductRepositoryOrator(ProductRepository):
    __table = 'products'
    __table_history = 'history_price'

    def __init__(self, db):
        self.db = db

    def get_all(self, request_objects):
        """
        Func to query get all
        :param request_objects: object from use case
        :return: list of row
        """
        query = self.db.table(self.__table)

        if request_objects.name != "":
            query = query.where('name', 'like', '%{}%'.format(request_objects.title))

        query = query.get()

        return list(map(lambda row: Product.from_dict(data=row), query))

    def get_total(self, request_objects):
        """
        Func to query get total row
        :param request_objects: objects from use case
        :return: total row
        """
        query = self.db.table(self.__table)

        if request_objects.name != "":
            query = query.where('name', '=', '{}'.format(request_objects.title))

        return query.count()

    def get_by_id(self, id):
        """
        Func to query data by id
        :param id: id product
        :return: object product
        """
        row = self.db.table(self.__table).where('id', id).first()
        return Product.from_dict(data=row) if row else None

    def get_by_url(self, url):
        """
        Func to query data by url
        :param url: url product
        :return: object product
        """
        row = self.db.table(self.__table).where('url', url).first()
        return Product.from_dict(data=row) if row else None

    def create(self, product):
        """
        Func to query insert
        :param product: object product from domain
        :return: last id
        """
        return self.db.table(self.__table).insert_get_id({
            'sku': product.sku,
            'name': product.name,
            'brand': product.brand,
            'image': product.image,
            'description': product.description,
            'width': product.width,
            'weight': product.weight,
            'height': product.height,
            'price': product.price,
            'price_currency': product.price_currency,
            'url': product.url,
            'created_at': helper.get_now_timestamp(),
            'updated_at': helper.get_now_timestamp(),
        })

    def update(self, product):
        """
        Func to query update
        :param product: object product from domain
        :return: bool
        """
        return self.db.table(self.__table).where('id', product.id).update({
            'sku': product.sku,
            'name': product.name,
            'brand': product.brand,
            'image': product.image,
            'description': product.description,
            'width': product.width,
            'weight': product.weight,
            'height': product.height,
            'price': product.price,
            'price_currency': product.price_currency,
            'url': product.url,
            'updated_at': helper.get_now_timestamp(),
        })

    def delete(self, id):
        """
        Func to query delete
        :param id: id product
        :return: bool
        """
        return self.db.table(self.__table).where('id', '=', id).delete()

    def create_price_history(self, data):
        """
        Insert price history to database
        :param data: dict of column & value table
        :return: last id
        """
        return self.db.table(self.__table_history).insert_get_id(data)

    def get_price_history(self, product_id):
        """
        Func to query get all
        :param product_id: product id
        :return: list of row
        """
        query = self.db.table(self.__table_history)
        query = query.where('product_id', product_id).order_by("id", "desc").get()

        return list(map(lambda row: PriceHistory.from_dict(data=row), query))
