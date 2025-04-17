import boto3

TABLE_NAME = "PokemonTeams"

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table(TABLE_NAME)

def print_movie(movie_dict):
    # print out the values of the movie dictionary
    print("Title: ", movie_dict["Title"])
    print(" Ratings: ", end="")
    for rating in movie_dict.get("Ratings"):
        print(rating, end=" ")
    print(" Year: ", movie_dict.get("Year"))
    print(" Number of Times Watched: ", movie_dict.get("TimesWatched"))
    print()

def print_all_movies():
    response = table.scan() #get all of the movies
    for movie in response["Items"]:
        print_movie(movie)