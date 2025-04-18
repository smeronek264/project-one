from src.pokemonDatabaseAccess import *
import boto3

TABLE_NAME = "PokemonTeams_PO"

dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
table = dynamodb.Table(TABLE_NAME)

def get_team(pokemon_team_dict):
    # print out the values of the movie dictionary
    pokemon_team = {}
    pokemon_team["team_name"] = pokemon_team_dict["team_name"]
    pokemon_list = []
    for pokemon in pokemon_team_dict.get("pokemon_numbers"):
        current_mon = showspecificpokemon(int(pokemon))
        current_mon = current_mon[0]
        pokemon_list.append(current_mon)  # don't reassign here

    pokemon_team["pokemons"] = pokemon_list

    
    return pokemon_team

def print_all_pokemon(table):
    response = table.scan() #get all of the movies
    teams = []
    for team in response["Items"]:
        teams.append(get_team(team))

    return teams

def create_teams(name, pokemon_list):
    try:
        table.put(Item = {"team_name":name, "pokemon_numbers":pokemon_list})
    except: raise("Can not add the team.")
    return None

def update_teams(name, pokemon_list):
    try:
        table.put(Item = {"team_name":name, "pokemon_numbers":pokemon_list})
    except: raise("Can not add the team.")
    return None

def delete_teams(name, pokemon_list):
    try:
        table.put(Item = {"team_name":name, "pokemon_numbers":pokemon_list})
    except: raise("Can not add the team.")
    return None



