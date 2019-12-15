import sys
sys.path.append(".")

from config.config import Config

DATABASES = {
    'default': {
        'driver': Config.DB_TYPE,
        'database': Config.DB_NAME,
        'prefix': ''
    }
}