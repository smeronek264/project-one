# author: Sophie Meronek
# description: This is a flask application that will allow for the user to look at different pokemons, 
# their weaknesses, and create different teams.
# credit: This code is based of code written by Prof. Moore Prof. Urness.  The templates were created using ChatGPT
# and previous work of mine from CS 188

# Importing all of the libraries
from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
import boto3
import creds
# importing scripts I had written.   These scripts are to access data from SQL and NOSQL databases on
# AWS
from src.pokemonDatabaseAccess import *
from src.teamDatabaseAccess import *

# Accessing my dynamodb database from AWS
TABLE_NAME = "PokemonTeams_PO"

dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
table = dynamodb.Table(TABLE_NAME)

# Initiating my flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

# This code will create a route to a home page that will allow the user to traverse
# through pokemon databases
@app.route('/')
def home():
    return render_template("home.html")

# This code will create a route to view all pokemon from a SQL database
@app.route('/showAllPokemon')
def show_all_pokemon():
    pokemon_list = allpokemonstats()
    return render_template('show-all-pokemon.html', pokemon_list=pokemon_list)

# This code will allow the user to fill out a form to filter the 
# the pokemon by their primary types
@app.route("/showPokemonForm", methods=['GET', 'POST'])
def show_pokemon_form():   
    return render_template('show-pokemon-type-form.html')

# This code will show the results of the form after it runs 
# a SQL query to show the pokemon with type1 = to their type
@app.route("/showPokemonType", methods=["GET", "POST"])
def show_pokemon():
    pokemon_type = request.form["type"]
    pokemon_list = showpokemon(pokemon_type)
    return render_template("show-pokemon.html", pokemon_list=pokemon_list)

# Will take the user to the team creator sections
# Will also be used to reroute after the user creates a team and 
# will run a query to create the team in the Dynamo DB
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

# This code will show all the teams that have been created 
# And when a team is deleted it will show that it has been deleted
@app.route("/showTeams", methods=['GET', 'POST'])
def get_pokemon_teams(): 

    if request.method == "POST":
        name = request.form["team_name"]
        
        delete_team(name)

        flash('Team has been deleted!', 'warning')

    team_list = print_all_pokemon(table)
    return render_template('show-teams.html', teams=team_list)

# This will allow the user to input the team name and pokemon 
# they want a team to be made up of
@app.route('/pokemonForm')
def pokemon_form():
    return render_template('pokemon-team-form.html')

# This will update the given team by the team name to a 
# precreated team (It would have taken user inputs, but it was being buggy)
@app.route("/updateTeam", methods=["GET", "POST"])
def update_team_page():
    if request.method == "POST":
        name = request.form["team_name"]
        pokemon = request.form["pokemon"]

        update_teams(table, name, pokemon)

        flash('Team has been updated',"warning" )


    return render_template('pokemon-team-update.html')

# This will delete the team if the name is given
@app.route("/deleteTeam")
def delete_team_page():
    return render_template('pokemon-team-delete.html')

# This will show how different types will do against certain pokemon, will
# call teh function that will do the JOIN query
@app.route("/pokemonDamage")
def pokemon_damage():
    damage_list = showdamagestats()
    return render_template("pokemon-damage.html", pokemon_list = damage_list)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)