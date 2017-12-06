from flask import request, render_template, session
from . import main
from .loginviews import is_logged_in
from ..models import Recipe, Dish
from flask_mail import Message
from flask_login import login_required

def send_email(to, subject, template, **kwargs):
	msg = Message(app.config['FY_MAIL_SUBJECT_PREFIX'] + subject,
	sender=app.config['FY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt', **kwargs)
	msg.html = render_template(template + '.html', **kwargs)
	mail.send(msg)

# from .forms import LoginForm

@main.route('/', methods=['GET','POST'])
@main.route('/index')
def index():
	# return render_template("profile_edit.html",menu="Edit Profile")
   	return render_template("homepage.html")
   	
@main.route('/myspace', methods=['GET','POST'])
# @login_required
def dashboard():
	return render_template("myspace.html")

@main.route("/recipe/<recipe_id>", methods=['GET','POST'])
def recipe(recipe_id):
	recipe = Recipe.objects.first()
	if (request.method == "POST"):
		value = int(request.form["rating"])
		rate = recipe.rate
		ppl = recipe.ppl
		new_rate = (rate * ppl +value) / (ppl+1)
		Recipe.objects(prl=recipe.prl).update_one(set__rate=new_rate)
		Recipe.objects(prl=recipe.prl).update_one(inc__ppl=1)
		return render_template("recipe.html",number=new_rate)

	return render_template("recipe.html",number = "{0:.1f}".format(recipe.rate))

@main.route("/recipe-upload",methods=['GET','POST'])
# @login_required
def uploadRecipe():
	# if (request.method == "POST"):
	# 	recipe = Recipe.objects(title=recipe_id)
	# 	dish = Dish(parent=recipe.title,prl=request.form["prl"],comment=request.form["message"])
	# 	dish.save()
	# 	return render_template("myrecipe.html")
	return render_template("uploadrecipe.html")

@main.route("/recipe/<recipe_id>/dish-upload",methods=['GET','POST'])
# @login_required
def uploadDish(recipe_id):
	if (request.method == "POST"):
		recipe = Recipe.objects(title=recipe_id)
		dish = Dish(parent=recipe.title,prl=request.form["prl"],comment=request.form["message"])
		dish.save()
		return render_template("mydish.html")
	return render_template("uploaddish.html")	
	
@main.route("/edit-profile",methods=['GET','POST'])
# @login_required
def editProfile():
	return render_template("editprofile.html")
	
@main.route("/myrecipe",methods=['GET','POST'])
# @login_required
def loadRecipe():
	return render_template("myrecipe.html")
	
@main.route("/mydish",methods=['GET','POST'])
# @login_required
def loadDish():
	return render_template("mydish.html")
	
@main.route("/following",methods=['GET','POST'])
# @login_required
def following():
	return render_template("myfollowing.html")