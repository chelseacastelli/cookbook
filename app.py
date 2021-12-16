
from flask import Flask, render_template, request, redirect, url_for
from helper import recipes, types, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from forms import RecipeForm, CommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route('/', methods=["GET", "POST"])
def index():
  #### Return a rendered index.html file
  return render_template('index.html', template_recipes=recipes)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  # Instantiate comment form
  comment_form = CommentForm(csrf_enabled=False)

  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)

    return redirect(url_for('recipe', id=id, _external=True))

  #### Return a rendered fried_egg.html file
  return render_template('recipe.html', template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], template_form=comment_form)

@app.route('/new-recipe', methods=["GET", "POST"])
def new_recipe():
  # Instantiate recipe form
  recipe_form = RecipeForm(csrf_enabled=False)

  if recipe_form.validate_on_submit():
    new_id = len(recipes) + 1
    #### Add the recipe name to recipes[new_id] and description to descriptions[new_id]
    recipes[new_id] = recipe_form.recipe.data
    types[new_id] = recipe_form.recipe_type.data
    descriptions[new_id] = recipe_form.description.data
    
    #### Add the values to new_ingredients and new_instructions
    new_ingredients = recipe_form.ingredients.data
    new_instructions = recipe_form.instructions.data
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
    comments[new_id] = []

    return redirect(url_for('recipe', id=new_id)) # _external=True, _scheme="https"

  return render_template('new_recipe.html', template_form=recipe_form)
