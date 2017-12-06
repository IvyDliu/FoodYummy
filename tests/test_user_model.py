import unittest
from app.models import User, Role, Permission

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User()
		u.password = 'word'
		self.assertTrue(u.p_hash is not None)

	def test_no_password_getter(self):
		u = User()
		u.password = 'word'
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User()
		u.password = 'word'
		self.assertTrue(u.verify_password('word'))
		self.assertFalse(u.verify_password('mord'))

	def test_password_salts_are_random(self):
		u1 = User()
		u1.password = 'word'
		u2 = User()
		u2.password = 'word'
		self.assertTrue(u1.p_hash != u2.p_hash)

	def test_email_confirmation(self):
		u = User(username = "john", email="123@gmail.com")
		u.password = '233'
		token = u.generate_confirmToken()
		self.assertTrue(u.confirm(token))
		self.assertTrue(u.confirmed)

	def test_role_admin(self):
		Role.insert_roles()
		u = User(username= "Tom", email="FoodYummy@gmail.com")
		u.password = "233"
		self.assertTrue(u.is_permitted(Permission.FOLLOW))
		self.assertTrue(u.is_permitted(Permission.MOD_COMMENT))
		self.assertTrue(u.is_admin())

	def test_role_user(self):
		Role.insert_roles()
		u = User(username= "Tom2", email="regular@gmail.com")
		u.password = "233"
		self.assertTrue(u.is_permitted(Permission.FOLLOW))
		self.assertFalse(u.is_permitted(Permission.MOD_COMMENT))
		self.assertFalse(u.is_admin())