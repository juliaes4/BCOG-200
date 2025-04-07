from flask import Flask, render_template, request
import csv

app = Flask(__name__)

# function: load_recipes(filepath)
# - loads recipe data from the CSV file
# - returns a dict of recipes

# function: search_recipe(query, recipes)
# - searches recipe dataset by keyword (ingredient, diet, flavor)
# - returns filtered dict of matches

# flask route: home()
# - handles GET and POST requests
# - returns rendered HTML template with filtered results

if __name__ == "__main__":
    app.run(debug=True)
#this is what everything would look like hypothetically.
