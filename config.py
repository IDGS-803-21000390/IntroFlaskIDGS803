import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY='Clave_Nueva'
    SESSION_COOKIE_SECURE=False


class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL='mysql+pymysql://nombreUsuario:root@127.0.0.1/prueba'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
#crear nuevo usuario en mysql