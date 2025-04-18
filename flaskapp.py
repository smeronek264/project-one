# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from src.pokemonDatabaseAccess import *
from src.teamDatabaseAccess import *
import boto3

TABLE_NAME = "PokemonTeams_PO"

dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
table = dynamodb.Table(TABLE_NAME)


app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/pokemonTeamCreator', methods = ["GET", "POST"])
def pokemon_creator_team():

    if request.method == "POST":
        name = request.form["team_name"]
        pokemon_list = []

        for pokemon in ["pokemon1", "pokemon1", "pokemon3", "pokemon4", "pokemon5", "pokemon6"]:
            if request.form[pokemon] != None:
                curr_pokemon = int(request.form[pokemon] )
                pokemon_list.append(curr_pokemon)

        create_teams(name, pokemon_list)

        flash('Team Successfully Added!', 'success')

    return render_template("pokemon-team-creator-menu.html")

@app.route('/showAllPokemon')
def show_all_pokemon():
    pokemon_list = allpokemonstats()
    return render_template('show-all-pokemon.html', pokemon_list=pokemon_list)

@app.route("/showPokemonForm", methods=['GET', 'POST'])
def show_pokemon_form():   
    return render_template('show-pokemon-type-form.html')

@app.route("/showTeams", methods=['GET', 'POST'])
def get_pokemon_teams():   
    team_list = print_all_pokemon(table)
    return render_template('show-teams.html', teams=team_list)

@app.route("/showPokemonType", methods=["GET", "POST"])
def show_pokemon():
    pokemon_type = request.form["type"]
    pokemon_list = showpokemon(pokemon_type)
    return render_template("show-pokemon.html", pokemon_list=pokemon_list)

@app.route('/pokemonForm')
def pokemon_form():
    return render_template('pokemon-team-form.html')

@app.route("/pokemonDamage")
def pokemon_damage():
    damage_list = showdamagestats()
    return render_template("pokemon-damage.html", pokemon_list = damage_list)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)