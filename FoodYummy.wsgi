#!flask/bin/python
import sys
 
sys.path.append('/Users/apple/OneDrive - McGill University/FoodYummy')
from app import create_app
application=create_app(config_name='default')