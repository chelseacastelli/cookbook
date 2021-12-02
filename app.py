
from flask import Flask, render_template, request
from helper import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions

app = Flask(__name__)

@app.route('/')
def index():
  #### Return a rendered index.html file
  return render_template('index.html', template_recipes=recipes)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route("/recipe/<int:id>")
def recipe(id):
  #### Return a rendered fried_egg.html file
  return render_template('recipe.html', template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id])

@app.route('/new-recipe', methods=["GET", "POST"])
def new_recipe():
  new_id = len(recipes) + 1
  if len(request.form) > 0:
    #### Add the recipe name to recipes[new_id] and description to descriptions[new_id]
    recipes[new_id] = request.form["recipe"]
    descriptions[new_id] = request.form["description"]
    
    #### Add the values to new_ingredients and new_instructions
    new_ingredients = request.form["ingredients"]
    new_instructions = request.form["instructions"]
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
    
  return render_template('new_recipe.html')
