from marshmallow import Schema, fields


class PriceHistoryBaseSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int()
    price = fields.Int()
    priceCurrency = fields.Str(attribute='price_currency')
    created = fields.Str(attribute='created_at')


class ProductBaseSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Int()
    sku = fields.Str()
    name = fields.Str()
    brand = fields.Str()
    image = fields.Str()
    description = fields.Str()
    width = fields.Str()
    weight = fields.Str()
    height = fields.Str()
    url = fields.Str()
    price = fields.Int()
    priceCurrency = fields.Str(attribute='price_currency')
    created = fields.Str(attribute='created_at')
    lastModified = fields.Str(attribute='modified_at')
    priceHistory = fields.Nested(PriceHistoryBaseSchema, attribute='price_history', many=True)
