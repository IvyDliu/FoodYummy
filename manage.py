#!flask/bin/python
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell

app = create_app(os.getenv('FY_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def test():
	""" Unit Tests """
	import unittest
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
	manager.run()