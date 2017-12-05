from flask import render_template, redirect, request, url_for, flash
from . import auth
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
		user.save()
		flash("You are now registered!", "success")
		# db.session.add(user)
		# dv.commit()
		token = user.generate_confirmToken()
		return redirect(url_for('auth.login'))
	return render_template('auth/register.html', form=form)
	
@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You are now logged out','success')
	return redirect(url_for('main.index'))
	
@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('main.index'))
	if current_user.confirm(token):
		flash('You are CONFIRMED!')
	else:
		flash('Invalid confirmation link')
	return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
	if current_user.is_authenticated:
		if not current_user.confirmed \
		and request.endpoint != 'auth' \
		and request.blueprint != 'auth' \
		and request.endpoint != 'static':
			return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
	if current_user.is_anonymous() or current_user.confirmed:
		return redirect(url_for('main.index'))
	return render_template("auth/unconfirmed.html",current_user=current_user)
	
@auth.route('/confirm')
@login_required
def resend_confirmation():
	token = current_user.generate_confirmToken()
	send_email(current_user.email, 'Confirm Your Account','auth/email/confirmation',user=current_user,token=token)
	flash('A new confirmation email has been sent to you by email.')
	return redirect(url_for('main.index'))