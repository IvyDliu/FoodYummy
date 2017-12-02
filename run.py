#!flask/bin/python
from app import create_app

create_app('default').run(debug=True)