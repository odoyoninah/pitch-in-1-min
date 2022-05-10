from distutils.command.config import config


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}