import os

SECRET_KEY = os.environ("SECRET_KEY")
MAIL_USERNAME = os.environ("MAIL_USERNAME")
MAIL_PASSWORD = os.environ("MAIL_PASSWORD")

ADMIN_USERNAME = os.environ('ADMIN_USERNAME')
ADMIN_EMAIL = os.environ('ADMIN_EMAIL')
ADMIN_PASSWORD = os.environ('ADMIN_PASSWORD')
ADMIN_ACCESS = os.environ('ADMIN_ACCESS')

class BaseConfig:
    SECRET_KEY = os.environ("SECRET_KEY")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ('MAIL_PASSWORD') 
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ('DEVELOPMENT_DATABASE_URI')
    LOGIN_DISABLED = False

class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ('TESTING_DATABASE_URI')
    LOGIN_DISABLED = True
    WTF_CSRF_ENABLED = False
    #SESSION_COOKIE_SECURE = False
    

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URI')