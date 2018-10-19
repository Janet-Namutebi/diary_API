import os

class BaseConfig:
    """
    Common configurations
    """
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.urandom(30)

class TestingConfig(BaseConfig):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    """
    Development configurations
    """

    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configurations
    """
    pass

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}