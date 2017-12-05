from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
# from flask_login import UserMixin
from . import login_manager
from app import db
from flask import current_app
import datetime

class Permission:
    ADMIN = 16
    MOD_COMMENT = 8
    WRITE_RECIPES = 4
    COMMENT = 2
    FOLLOW = 1

class Role(db.Document):
    name = db.StringField(max_length=50,unique=True)
    default = db.BooleanField(default=False,index=True)
    permissions = db.IntField(default=0)

    @staticmethod
    def insert_roles():
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE_RECIPES],
            'Admin': [Permission.FOLLOW, Permission.COMMENT, 
            Permission.WRITE_RECIPES,Permission.MOD_COMMENT, Permission.ADMIN],
        }
        for r in roles:
            role = Role.objects(name=r).first()
            if role is None:
                role = Role(name=r)
                role.set_permission(roles.get(r))
                role.default = (role.name == 'User')
                role.save()

    def set_permission(self, perms):
        for p in perms:
            self.permissions += p

    def remove_permission(self, perms):
        for p in perms:
            self.permission -= p

    def is_permitted(self, p):
        return (self.permissions & p == p)

class User(db.Document): 
    id = db.SequenceField(primary_key=True)
    email = db.StringField(required=True,unique=True,index=True)
    username = db.StringField(max_length=50,required=True,index=True)
    p_hash = db.StringField(max_length=128,required=True)
    confirmed = db.BooleanField(default=False)
    role = db.ReferenceField(Role)

    def __init__(self,**kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FY_ADMIN']:
                self.role = Role.objects(name='Admin').first()
            else:
                self.role = Role.objects(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.p_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.p_hash, password)

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
        self.save()
        return True

    def is_permitted(self, permission):
        return self.role is not None and self.role.is_permitted(permission)

    def is_admin(self):
        return self.is_permitted(Permission.ADMIN)

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()


class Dish(db.DynamicDocument):
    parent = db.StringField(required=True)
    prl = db.StringField(required=True)
    author = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    comment = db.StringField(max_length=1200)


class Recipe(db.DynamicDocument):
    title = db.StringField(max_length=120, required=True)
    author = db.ReferenceField(User, reverse_delete_rule=CASCADE)
    prl = db.StringField(required=True)
    desc = db.StringField(max_length=200, required=True)
    ing = db.StringField(max_length=200, required=True)
    step = db.StringField(required=True)
    

    region = db.StringField(max_length=40, required=True)
    ming = db.StringField(max_length=40, required=True)
    kind = db.StringField(max_length=40, required=True)

    works = db.ListField(ReferenceField(Dish))
    ts  = db.DateTimeField(default=datetime.datetime.now)
    rate = db.DecimalField(default=0.0,precision=1)
    ppl = db.IntField(default=1)
    def get_recipe():
        return Recipe.objects().first()

