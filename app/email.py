from threading import Thread
from flask_mail import Message
from flask import render_template, current_app
from app import create_app, mail

def send_async_email(app, msg):
	app = create_app('default')
	with app.app_context():
		mail.send(msg)

def send_email(to, subject, template, **kwargs):
	msg = Message(current_app.config['FY_MAIL_SUBJECT_PREFIX'] + subject, sender=current_app.config['FY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	thr = Thread(target=send_async_email, args=[current_app, msg])
	thr.start()
	return thr