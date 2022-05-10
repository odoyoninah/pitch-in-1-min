from distutils.command.config import config


class Config:
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}