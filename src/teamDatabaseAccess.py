# author: Sophie Meronek and CHATGPT
# This file is meant to access the dynamo DB database and will return different data


from src.pokemonDatabaseAccess import *
import boto3

TABLE_NAME = "PokemonTeams_PO"

dynamodb = boto3.resource('dynamodb', region_name="us-east-2")
table = dynamodb.Table(TABLE_NAME)


# This will read in a team that shows up in the Dynamo DB
# This will get each team, and create the list of pokemon with the 
# poke numbers that are included
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

# Will iterate through all possible pokemon teams
def print_all_pokemon(table):
    response = table.scan() #get all of the movies
    teams = []
    for team in response["Items"]:
        teams.append(get_team(team))

    return teams

# This will take in a list of pokemon and name and 
# insert the data in the database
def create_teams(name, pokemon_list):
    try:
        table.put_item(Item = {"team_name":name, "pokemon_numbers":pokemon_list})
        return None

    except: 
       return "<p>Can not add the team.</p>"

# This will update the team make up with a predetermined
# team
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

# This will delete a team when given the team_name
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





