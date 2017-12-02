from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_login import UserMixin
from . import login_manager
from app import db
from flask import current_app
import datetime

class User(db.Document):
    id = db.IntField(unique=True,primary_key=True)
    email = db.StringField(required=True,unique=True,index=True)
    username = db.StringField(max_length=50,required=True,index=True)
    password = db.StringField(max_length=128,required=True)
    confirmed = db.BooleanField(default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def generate_confirmToken(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'],expiration)
        return s.dumps({'confirm':self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
#         db.session.add(self)
		return True

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

class Role(db.Document):
    id = db.IntField(unique=True,primary_key=True)
    name = db.StringField(max_length=50,required=True)
    users = db.ListField(ReferenceField(User))


class Dish(db.Document):
    parent = db.StringField(required=True)
    prl = db.StringField(required=True)
    author = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    comment = db.StringField(max_length=1200)


class Recipe(db.Document):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    prl = db.StringField(required=True)
    region = db.StringField(max_length=40)
    ing = db.StringField(max_length=40)
    kind = db.StringField(max_length=40)
    works = db.ListField(ReferenceField(Dish))
    ts  = db.DateTimeField(default=datetime.datetime.now)
    rate = db.DecimalField(default=0.0,precision=1)
    ppl = db.IntField(default=1)
    def get_recipe():
        return Recipe.objects().first()

