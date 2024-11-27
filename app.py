from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    with open('recipes.json') as f:
        recipes = json.load(f)
    return render_template('index.html', recipes=recipes)

if __name__ == '__main__':
    app.run(debug=True)