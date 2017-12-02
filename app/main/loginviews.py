from flask import render_template,flash,redirect, request, session
from app import db
from .forms import LoginForm, RegisterForm
from functools import wraps
from . import main



@main.route('/register', methods = ['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == "POST" and form.validate():
		username = form.username.data
		#add encryption here
		password = form.password.data
		email = form.email.data
		users = db.users
		users.insert({'username':username, 'password':password,'email':email})
		flash("You are now registered!", "success")
		return redirect(url_for("main.index"))
	return render_template("register.html", form=form)
	
@main.route('/login',methods = ['GET', 'POST'])
def login():
	if request.method == 'POST':
	
		username = request.form['email']
		password_input = request.form['password']
		
		# mongodb
		users = db.users
		user = users.find_one({"name":username})		
		
		if user is None:
			error = 'Username not found'
			return render_template('login.html',error=error)
		else:
			password = user['password']
			if password == password_input:
				# log in success
				session['logged_in'] = True
				session['username'] = username
				
				flash('You are now logged in', 'success')
				return redirect(url_for('dashboard'))
				
			else:
				error = 'Password Invalid'
				return render_template('login.html',error=error)
		
	return render_template('login.html')
	
def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'loggef_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please log in first','danger')
			return redirect('login')
	return wrap
	
	
@main.route('/logout')
def logout():
	session.clear()
	flash('You are now logged out','success')
	return redirect('login')
		
