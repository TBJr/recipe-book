import json
from jinja2 import Environment, FileSystemLoader

# Load recipes from JSON
with open('recipes.json') as f:
    recipes = json.load(f)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Render index.html
index_template = env.get_template('index.html')
rendered_index = index_template.render(recipes=recipes)

# Save the rendered HTML
with open('build/index.html', 'w') as f:
    f.write(rendered_index)

# Similarly, render other templates if needed