#!flask/bin/python
from app import create_app

myapp = create_app('default').run(debug=True)