class Config(object):
    SECRET_KEY = ''

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:YOURPASSWORD@120.79.139.82:3306/rooprint"
