from flask import Flask, render_template
from flask_mail import Mail
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from config import config
from flask_login import LoginManager

db = MongoEngine()
mail = Mail()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])
	config[config_name].init_app(app)
	mail.init_app(app)
	db.init_app(app)
	app.session_interface = MongoEngineSessionInterface(db)
	login_manager.init_app(app)
	
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint, url_prefix='/auth')
	

	return app
