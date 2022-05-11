import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #my app configuration.
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hello-world'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'weather.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    