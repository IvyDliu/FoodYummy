import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:

	WTF_CSRF_ENABLED = True
	SECRET_KEY = os.urandom(24)

	FY_MAIL_SUBJECT_PREFIX = 'Dear User: '
	FY_MAIL_SENDER = '[FoodYummy] <duoduo.liu@mail.mcgill.com>'
	FY_ADMIN = os.environ.get('FY_ADMIN')

	@staticmethod
	def init_app(app):
		pass
		
class DevelopmentConfig(Config):
	DEBUG = True
	MAIL_SERVER ='smtp.gmail.com'
	MAIL_PORT = 465
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	MAIL_USE_TLS = False
	MAIL_USE_SSL = True
	# Config MongoDB
	MONGO_URI = 'mongodb://localhost:27017/FoodYummy'
	MONGODB_DB = 'FoodYummy'

class TestingConfig(Config):
	TESTING = True
	# PRESERVE_CONTEXT_ON_EXCEPTION = False
	MONGO_URI = 'mongomock://localhost:27017/testdb'

config = {
'development': DevelopmentConfig,
'testing': TestingConfig,
'default': DevelopmentConfig
}