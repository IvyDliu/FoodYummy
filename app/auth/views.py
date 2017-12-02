from flask import render_template, redirect, request, url_for, flash
from . import auth
from flask_login import login_user, logout_user, login_required
from .forms import LoginForm, RegisterForm
from ..models import User
from ..email import send_email

@auth.route('/login',methods = ['GET', 'POST'])
def login():
	form = LoginForm(request.form)
	if request.method == 'POST' and form.validate():
		user = form.get_user()
		if user is not None:
			if user.verify_password(form.password.data):
				login_user(user, form.remember_me.data)
				return redirect(request.args.get('next') or url_for("main.dashboard"))
			else:
				error = 'Password Invalid'
				return render_template('auth/login.html',error=error)				
		else:
			error = 'Username not found'
			return render_template('auth/login.html',error=error)
	elif request.method == 'POST' and form.validate() == False:
		error = "Not Validated"
		return render_template('auth/login.html',error=error)
	return render_template('auth/login.html',form=form)

@auth.route('/register', methods = ['GET','POST'])
def register():
	form = RegisterForm(request.form)
	if request.method == "POST" and form.validate():
		user = User(email=form.email.data,
		username=form.username.data)
		user.set_password(form.password.data)
		user.save()
		flash("You are now registered!", "success")
		# db.session.add(user)
		# dv.commit()
		token = user.generate_confirmToken()
		send_email(user.email, 'Confirm Your Account','auth/email/confirm',user=user,token=token)
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)

def is_logged_in(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('Please log in first','danger')
			return redirect('login')
	return wrap
	
	
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You are now logged out','success')
	return redirect(url_for('main.index'))