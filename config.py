import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config(object):
	DEBUG=False
	TESTING = False
	CSRF_ENABELD = True
	SECRET_KEY='thisisthesecretkey1234567890'

class ProductionConfig(Config):
	DEBUG=False

class DevelopmentConfig(Config):
	DEBUG=True
	TESTING = True
