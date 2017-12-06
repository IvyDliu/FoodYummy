from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors
from ..models import Permission

@main.app_context_processor
def include_permissions():
	return dict(Permission=Permission)