# change the flask default initialization parameters

class Config(object):
    DEBUG: bool = False
    TESTING: bool = False
    # avoid client manipulation of session data.
    SECRET_KEY: str = b'R\xdb\x15\x01_\x7f\xb8\x8eX\xf9\xbe\x15\x9c\x98\x17\x8d\x18H\xbc\x8b\xbe\x0f\xc9\xb8'


class ProductionConfig(Config):
    FLASK_ENV = "production"


class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG: bool = True


class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING: bool = True
