from flask import Flask, render_template, jsonify, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('recipes.json') as f:
        recipes = json.load(f)
    return render_template('/index.html', recipes=recipes)

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

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    with open('recipes.json') as f:
        recipes = json.load(f)
    filtered_recipes = [recipe for recipe in recipes if query.lower() in recipe['name'].lower()]
    return render_template('index.html', recipes=filtered_recipes)

if __name__ == '__main__':
    app.run(debug=True)