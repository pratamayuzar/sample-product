"""
App sanic
"""
import logging

from orator import DatabaseManager
from sanic import Sanic
from sanic_cors import CORS

from config.config import Config
from src.products.v1.delivery.http_sanic import bp_products

LOGGER = logging.getLogger(__name__)


def config_log():
    """
    Set config log
    :param app: sanic app
    :return: None
    """
    # set log config from config
    logging.config.dictConfig(Config.LOGGING)


def connect_db():
    """
    Set initial db connect
    :return: DatabaseManager orator
    """
    config = {
        'default': {
            'driver': Config.DB_TYPE,
            'database': Config.DB_NAME,
            'prefix': '',
            'log_queries': True,
        }
    }
    return DatabaseManager(config)


def create_app(config):
    """
    Set blueprint for app sanic
    :param config: config decouple
    :return: app sanic
    """
    app = Sanic(__name__)
    app.config.from_object(config)
    app.blueprint(bp_products)
    CORS(app, automatic_options=True)

    return app
