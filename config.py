import os
from distutils.command.config import config



class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql= psycopg2://moringa:1234@localhost/Pitch_in_1_min"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}