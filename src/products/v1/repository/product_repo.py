"""
Abstract for Product Repository
"""
from abc import ABC, abstractmethod


class ProductRepository(ABC, object): # pragma: no cover

    @abstractmethod
    def get_all(self, filters): pass

    @abstractmethod
    def get_total(self, filters): pass

    @abstractmethod
    def get_by_id(self, pk): pass

    @abstractmethod
    def get_by_url(self, url): pass

    @abstractmethod
    def create(self, data): pass

    @abstractmethod
    def update(self, data): pass

    @abstractmethod
    def delete(self, data): pass

    @abstractmethod
    def create_price_history(self, data): pass

    @abstractmethod
    def get_price_history(self, product_id): pass
