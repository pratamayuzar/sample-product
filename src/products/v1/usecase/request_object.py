from src.shared import helper
from src.shared.request_object import ValidRequestObject, InvalidRequestObject


class ProductCreateRequestObject(ValidRequestObject):
    def __init__(self, url):
        self.url = url

    @classmethod
    def from_dict(cls, data):

        # TODO : add validation if needed
        errors = dict()
        url = helper.get_value_from_dict(data, 'url', '')
        if not url:
            errors.update({'url': 'is required'})

        if 'fabelio.com/ip' not in url:
            errors.update({'url': 'is not fabelio product url'})

        if errors:
            invalid_req = InvalidRequestObject()
            invalid_req.parse_error(errors=errors)
            return invalid_req

        return cls(
            url=url
        )


class ProductListRequestObject(ValidRequestObject):
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, data):

        # TODO : add validation if needed

        return cls(
            name=helper.get_value_from_dict(data, 'name', '')
        )


class ProductDetailRequestObject(ValidRequestObject):
    def __init__(self, id, crawl):
        self.id = id
        self.crawl = crawl

    @classmethod
    def from_dict(cls, data):

        # TODO : add validation if needed

        return cls(
            id=data['id'],
            crawl=data.get('crawl')
        )
