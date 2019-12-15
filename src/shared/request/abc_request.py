from abc import ABC, abstractmethod


class Request(ABC, object):  # pragma: no cover

    @abstractmethod
    def form_to_dict(): pass

    @abstractmethod
    def json_to_dict(): pass

    @abstractmethod
    def query_to_dict(): pass

    @abstractmethod
    def parse_all_to_dict(): pass
