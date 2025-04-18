# author: Sophie Meronek and CHATGPT
# This code will access the SQL data on the RDS
# It will run different queries to access different parts of the data

import pymysql
import pymysql.cursors
import creds

# This function will connect to the sql server
def get_conn():

    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )

# This function will run the queries I write
def execute_query(query,args=()):

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query,args)
            rows=cur.fetchall()
        return rows
    finally:
        conn.close()


# This query will show all the pokemon of a specific type enter in by the user
def showpokemon(poke_type):
    query = "SELECT pokedex_number, name, type1 FROM Pokemon WHERE type1 = %s;"
    return execute_query(query, (poke_type,))

# This query will show all the pokemon with their name and pokenumber
# It isn't really used at all.   Was going to use it to make the team creation easier
def allpokemon():
    query = "SELECT pokedex_number, name FROM Pokemon;"
    return execute_query(query)

# This will show all of the pokemons with their primary type, hit points, attack, defense
# special attack, and special defense
def allpokemonstats():
    query = "SELECT pokedex_number, name, type1, hp, attack, defense, sp_attack, sp_defense FROM Pokemon;"
    return execute_query(query)

# THIS QUERY UTILIZES THE JOIN FUNTION
# The query will out put all fo the pokemon's weaknesses and strengths
# It will only show 200 records because both of hte pokedex_numbers must be present in the two different
# tables
def showdamagestats():
    query = "SELECT Pokemon.pokedex_number, name, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel, against_water FROM Pokemon JOIN Pokemon_Damage WHERE Pokemon.pokedex_number = Pokemon_Damage.pokedex_number;"
    
    return execute_query(query)

# This function will take a specific pokedex_number and output the pokemon name and type
# It will only return if the number is in the table, else it will return none.
def showspecificpokemon(pokedex_number):
    query = "SELECT pokedex_number, name, type1 FROM Pokemon WHERE pokedex_number = %s;"
    return execute_query(query, (int(pokedex_number),))


        
    
