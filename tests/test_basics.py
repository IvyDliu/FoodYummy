import unittest
from flask import current_app
from app import create_app
import mongoengine as me

class BasicsTestCase(unittest.TestCase):
	def setUp(self):
		
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.db = me.connect('testdb',host='mongomock://localhost')
		self.app_context().push()

	def tearDown(self):
		self.db.drop_database('testdb')
		self.db.close()
		self.app_context().pop()

	
	def test_app_exists(self):
		self.assertFalse(current_app is None)

	def test_app_is_testing(self):
		self.assertTrue(current_app.config['TESTING'])
