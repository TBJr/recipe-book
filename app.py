from flask import Flask, render_template, jsonify, request, redirect, url_for
import json

app = Flask(__name__)

def load_recipes():
    with open('recipes.json') as f:
        return json.load(f)

def save_recipes(recipes):
    with open('recipes.json', 'w') as f:
        json.dump(recipes, f)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    with open('recipes.json') as f:
        recipes = json.load(f)
    filtered_recipes = [recipe for recipe in recipes if query.lower() in recipe['name'].lower()]
    return render_template('index.html', recipes=filtered_recipes)

@app.route('/')
def index():
    recipes = load_recipes()
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        new_recipe = {
            "name": request.form['name'],
            "description": request.form['description']
        }
        with open('recipes.json', 'r+') as f:
            recipes = json.load(f)
            recipes.append(new_recipe)
            f.seek(0)
            json.dump(recipes, f)
        return redirect(url_for('index'))
    return render_template('add_recipe.html')

@app.route('/edit/<int:recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipes = load_recipes()
    recipe = recipes[recipe_id]

    if request.method == 'POST':
        recipe['name'] = request.form['name']
        recipe['description'] = request.form['description']
        save_recipes(recipes)
        return redirect(url_for('index'))

    return render_template('edit_recipe.html', recipe=recipe, recipe_id=recipe_id)

@app.route('/delete/<int:recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
    recipes = load_recipes()

    if request.method == 'POST':
        recipes.pop(recipe_id)
        save_recipes(recipes)
        return redirect(url_for('index'))

    recipe = recipes[recipe_id]
    return render_template('delete_recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)