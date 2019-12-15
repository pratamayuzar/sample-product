class Product(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.sku = kwargs.get('sku')
        self.name = kwargs.get('name')
        self.brand = kwargs.get('brand')
        self.image = kwargs.get('image')
        self.description = kwargs.get('description')
        self.width = kwargs.get('width')
        self.height = kwargs.get('height')
        self.weight = kwargs.get('weight')
        self.price = kwargs.get('price')
        self.price_currency = kwargs.get('price_currency')
        self.url = kwargs.get('url')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    @classmethod
    def from_dict(cls, data):
        article = cls(**{
            "id": data.get('id'),
            "sku": data.get('sku'),
            "name": data.get('name'),
            "brand": data.get('brand'),
            "image": data.get('image'),
            "description": data.get('description'),
            "width": data.get('width'),
            "height": data.get('height'),
            "weight": data.get('weight'),
            "price": data.get('price'),
            "price_currency": data.get('price_currency'),
            "url": data.get('url'),
            "created_at": data.get('created_at'),
            "updated_at": data.get('updated_at')
        })

        return article


class PriceHistory(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.product_id = kwargs.get('product_id')
        self.price = kwargs.get('price')
        self.price_currency = kwargs.get('price_currency')
        self.created_at = kwargs.get('created_at')
        self.updated_at = kwargs.get('updated_at')

    @classmethod
    def from_dict(cls, data):
        article = cls(**{
            "id": data.get('id'),
            "product_id": data.get('product_id'),
            "price": data.get('price'),
            "price_currency": data.get('price_currency'),
            "created_at": data.get('created_at'),
            "updated_at": data.get('updated_at')
        })

        return article
