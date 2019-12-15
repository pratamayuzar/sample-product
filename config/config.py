import os

from decouple import config


class Config(object):
    """
    Base configuration
    """
    DEBUG = config('DEBUG') == 'True'
    HOST = config('HOST')
    PORT = config('PORT')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    RUN_MULTIPLE_PROCESS = config('RUN_MULTIPLE_PROCESS') == 'True'

    DB_TYPE = config('DB_TYPE')
    DB_NAME = config('DB_NAME')

    SUCCESS = 'SUCCESS'
    RESOURCE_ERROR = 'RESOURCE_ERROR'
    PARAMETERS_ERROR = 'PARAMETERS_ERROR'
    SYSTEM_ERROR = 'SYSTEM_ERROR'
    DATA_NOT_FOUND = 'DATA_NOT_FOUND'

    STATUS_CODES = {
        SUCCESS: 200,
        DATA_NOT_FOUND: 204,
        RESOURCE_ERROR: 404,
        PARAMETERS_ERROR: 400,
        SYSTEM_ERROR: 500,
    }

    HTTP_STATUS_CODES = {
        100:    'Continue',
        101:    'Switching Protocols',
        102:    'Processing',
        200:    'OK',
        201:    'Created',
        202:    'Accepted',
        203:    'Non Authoritative Information',
        204:    'No Content',
        205:    'Reset Content',
        206:    'Partial Content',
        207:    'Multi Status',
        226:    'IM Used',              # see RFC 3229
        300:    'Multiple Choices',
        301:    'Moved Permanently',
        302:    'Found',
        303:    'See Other',
        304:    'Not Modified',
        305:    'Use Proxy',
        307:    'Temporary Redirect',
        400:    'Bad Request',
        401:    'Unauthorized',
        402:    'Payment Required',     # unused
        403:    'Forbidden',
        404:    'Not Found',
        405:    'Method Not Allowed',
        406:    'Not Acceptable',
        407:    'Proxy Authentication Required',
        408:    'Request Timeout',
        409:    'Conflict',
        410:    'Gone',
        411:    'Length Required',
        412:    'Precondition Failed',
        413:    'Request Entity Too Large',
        414:    'Request URI Too Long',
        415:    'Unsupported Media Type',
        416:    'Requested Range Not Satisfiable',
        417:    'Expectation Failed',
        418:    'I\'m a teapot',  # see RFC 2324
        422:    'Unprocessable Entity',
        423:    'Locked',
        424:    'Failed Dependency',
        426:    'Upgrade Required',
        428:    'Precondition Required',  # see RFC 6585
        429:    'Too Many Requests',
        431:    'Request Header Fields Too Large',
        449:    'Retry With',  # proprietary MS extension
        451:    'Unavailable For Legal Reasons',
        500:    'Internal Server Error',
        501:    'Not Implemented',
        502:    'Bad Gateway',
        503:    'Service Unavailable',
        504:    'Gateway Timeout',
        505:    'HTTP Version Not Supported',
        507:    'Insufficient Storage',
        510:    'Not Extended'
    }

    TIME_ZONE = 'Asia/Jakarta'

    SENTRY_DSN = config("SENTRY_DSN", default="")

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'console': {
                'format': '[%(asctime)s][%(levelname)s] %(name)s '
                          '%(filename)s:%(funcName)s:%(lineno)d | %(message)s',
                'datefmt': '%H:%M:%S',
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'console'
            },
            'sentry': {
                'level': 'ERROR',
                'class': 'raven.handlers.logging.SentryHandler',
                'dsn': SENTRY_DSN,
            },
        },
        'loggers': {
            '': {
                'handlers': ['console', 'sentry'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'your_app': {
                'level': 'DEBUG',
                'propagate': True,
            }
        }
    }
