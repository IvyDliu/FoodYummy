Project: FoodYummy
A website for you to explore world wide recipes and dishes.

Group Members
Duoduo (Ivy) Liu, Lu Ya Ding, Zhesheng (Helen) Gu

Technology
Front-end	Back-end
+ HTML	+ Apache
+ CSS	+ Flask
+ Javascript/DOM	+ Python
+ JSON	+ Mongodb
+ Ajax	+ Mongoengine
+ JQuery	+ Security
+ Bootstrap	
+ React	
+ Babel	
Deploy FoodYummy on Your Computer
Requirement Make sure you have following: MAC OSX 10.7+, Python2.7+, MongoDB 3.4, Apache 2.4 folder structure
    +\FoodYummy
		-all backend1.zip files
		-\app
				-all backend2.zip files
				-all frontend.zip files
Install Dependencies a) mod_wsgi Follow this: https://modwsgi.readthedocs.io/en/develop/user-guides/installation-on-macosx.html Then in httpd.config

 DocumentRoot “PATH/TO/YOUR/FOODYUMMY”
 WSGIScriptAlias / “PATH/TO/YOUR/FOODYUMMY/FoodYummy.wsgi"
<Directory “PATH/TO/YOUR/FOODYUMMY”> Require all granted Allow from all

b) from command line, enter: $ cd FoodYummy $ source setup.sh $ pip install -r requirements.txt c) in FoodYummy.wsgi replace sys.path.append() to sys.path.append(“PATH/TO/YOUR/FOODYUMMY”)

Run server # first run mongodb with - - dbpath PATH/TO/FOODYUMMY/database $ httpd.exe -k start $ cd FoodYummy $ python manage.py runserver

To use unit test, type $ python manage.py test

How to Use Our Website
from browser, type: localhost/
You can search our recipe using filter
You can view our recipe by clicking on the pictures
You can send us email by filling a contact form
If you want to explore more features, you can log in/register
You need to confirm the email address to register
After log in, you can view your dashboard
You can also upload your own recipe and dish
Enjoy! If any questions during installation, please contact us at foodyummy307@gmail.com
