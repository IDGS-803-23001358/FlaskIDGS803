from re import DEBUG


from sqlalchemy import create_engine

class Config(object):
    SECRET_KEY="ClaveSecreta"
    SSESION_COOKIE_SECURE=False
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:michelle1304@127.0.0.1:3306/bdigs803'
    SCHALCHEMY_TRACK_MODIFICATIONS=False