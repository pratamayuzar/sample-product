from src.shared.request.abc_request import Request
from config.config import Config


class RequestSanicDict(Request):

    def __init__(self, request):
        self.request = request
        super(RequestSanicDict, self).__init__()

    def form_to_dict(self):
        dict_d = {}
        try:
            for key in dict(self.request.form):
                dict_d[key] = self.request.form.get(key, '')
        except Exception as e:
            pass

        return dict_d

    def json_to_dict(self):
        dict_d = {}
        try:
            dict_d.update(self.request.json)
        except Exception as e:
            pass

        return dict_d

    def query_to_dict(self):
        dict_d = {}
        try:
            dict_d.update(self.request.raw_args)
        except Exception as e:
            pass

        return dict_d

    def parse_all_to_dict(self):
        dict_d = {}
        try:
            dict_d.update(self.json_to_dict())
            dict_d.update(self.form_to_dict())
            dict_d.update(self.query_to_dict())
        except Exception as e:
            pass

        return dict_d
