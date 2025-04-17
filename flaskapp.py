# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from src.pokemonDatabaseAccess import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/pokemonTeamCreator')
def pokemon_creator_team():
    return render_template("pokemon-team-creator-menu.html")

@app.route('/showAllPokemon')
def show_all_pokemon():
    pokemon_list = all_pokemon_stats()
    return render_template('show-all-pokemon.html', pokemon_list=pokemon_list)

# @app.route("/showPokemonForm", methods=['GET', 'POST'])
# def show_pokemon_form():
#     if request.method == "POST":
#         pokemon_type = request.form["type"]
#         return redirect(url_for('show_pokemon', pokemon_type=pokemon_type))
    
#     else:
#         return render_template('show-pokemon-type-form.html')

@app.route("/showPokemonForm", methods=['GET', 'POST'])
def show_pokemon_form():
    if request.method == "POST":
        pokemon_type = request.form["type"]
        print(f"Redirecting to show_pokemon with type: {pokemon_type}")  # Debugging line
        return redirect(url_for('show_pokemon', pokemon_type=pokemon_type))    
    return render_template('show-pokemon-type-form.html')


@app.route("/showPokemonType", methods=["GET, POST"])
def show_pokemon(pokemon_type):
    pokemon_list = showpokemon(pokemon_type)
    return render_template("show-pokemon.html", pokemon_list=pokemon_list)

@app.route('/pokemonForm')
def pokemon_form():
    pokemon_list = all_pokemon()
    return render_template('pokemon_team_form.html', pokemon_list = pokemon_list)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)