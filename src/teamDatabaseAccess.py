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
    for pokemon in pokemon_team_dict.get("pokemon_numbers", []):
        try:    
            current_mon = showspecificpokemon(int(pokemon))
            if current_mon and len(current_mon) > 0:
                pokemon_list.append(current_mon[0])
            else:
                print(f"Warning: No data found for Pokémon #{pokemon}")
        except: 
            print("No Pokemon")


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
        table.put_item(Item = {"team_name":name, "pokemon_numbers":pokemon_list})
        return None

    except: 
       return "<p>Can not add the team.</p>"

def update_teams(table, name, pokemon):
    teams = print_all_pokemon(table)
    for team in teams:
        if team["team_name"] == name:
            pokemon_list = [12, 56, 36, 95, 78, 456]

            table.update_item(
                Key={"team_name": name},
                UpdateExpression="SET pokemon_numbers = :r",
                ExpressionAttributeValues={':r': pokemon_list}
            )

def delete_team(team_name):
    """
    prompt user fora Movie Title
    delete item from the database
    """
    try:
        table.delete_item(
            Key = {
                'team_name':team_name
            }
        )
        
    except:
        print("error in deleting movie")





