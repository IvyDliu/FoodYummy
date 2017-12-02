12345678
#### Install Flask
^^_^^
>> https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
1. create project folder “/abc/FoodYummy” and go to it.
`cd /abc/FoodYummy`
2. install flask and flask modules you want to use
`python -m env flask`
if python —version==2.7, install virtualenv first
`sudo easy_install virtualenv`
`virtualenv flask`
now under “/FoodYummy” there is a “/flask” folder
install flask and its dependency
`flask/bin/pip install flask`
`flask/bin/pip install flask-wtf`
`flask/bin/pip install flask_pymongo`
(modules I used so far)
3. create following project structure

	FoodYummy
		|_activate
		|_app
			|_static
			|_templates
				|- //our template codes
			|- //our views
			|- “__init__.py”
		|_database
		|_flask
		|_tmp
		|_ “config.py”
		|_ “run.py”					//some folders are already there

#### Install Mongodb
1. download community server (with SSL) at https://www.mongodb.com/download-center and unzip to /FoodYummy
2. rename the folder to “/mongodb”

#### Launch Flask and use Mongoldb
1. in run.py
	
	#!flask/bin/python
	from app import app
	app.run(debug=True)

2. in __init__.py
	
	from flask import Flask
	from flask_pymongo import PyMongo

	app = Flask(__name__)
	app.config.from_object('config')
	mongo = PyMongo(app)

	from app import views
	
3. in config.py
	
	WTF_CSRF_ENABLED = True
	SECRET_KEY = “some string“
	# I don’t know what’s this for

3. in views.py
	
	from flask import render_template
	from app import app

	@app.route('/')
	@app.route('/index')

	def index():
    		from pymongo import MongoClient
    		client = MongoClient('localhost:27017')
    		db = client.myFirstMB
    		# add an entry
    		db.countries.insert({"name" : "US"})
    		return '''
        <html>
        <head>
        <title>Home Page</title>
        </head>
        <body>
        <h1>Hello, ''' + str(db.countries.find_one()) + '''</h1>
            </body>
            </html>
            '''

4. launch mongodb first:
	`mongod —dbpath “\abc\FoodYummy”`
5. then launch flask:
	`python run.py`
6. check in your browser
	`http://localhost:5000/index`
	should print “Hello,{u’id…..}”



	

	
