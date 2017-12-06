from flask import request, render_template, session
from . import main
from ..models import Recipe, Dish
from flask_login import login_required

@main.route('/', methods=['GET','POST'])
def index():
	return render_template("homepage.html")
	# return render_template("500.html",confirm="yes")
   	
@main.route('/myspace', methods=['GET','POST'])
# @login_required
def dashboard():
	return render_template("myspace.html")

@main.route("/recipe/<recipe_id>", methods=['GET','POST'])
def recipe(recipe_id):
	recipe = Recipe.objects.first()
	if (request.method == "POST"):
		author=recipe.author
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
	# 	recipe = Recipe(title="request.form[""]",prl=request.form["prl"],comment=request.form["message"],author=)
	# 	recipe.save()
	# 	return render_template("myrecipe.html")
	return render_template("uploadrecipe.html")

@main.route("/recipe/<recipe_id>/dish-upload",methods=['GET','POST'])
# @login_required
def uploadDish(recipe_id):
	if (request.method == "POST"):
		recipe = Recipe.objects(title=recipe_id)
		dish = Dish(parent=recipe.title,author="",prl=request.form["prl"],comment=request.form["message"])
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