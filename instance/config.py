
class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
class DevelopmentConfig(Config):
    DB_SERVER = 'localhost'
    DEBUG = True
    RETURN_URL='127.0.0.1'