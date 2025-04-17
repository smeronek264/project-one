import pymysql
import pymysql.cursors
import creds

def get_conn():

    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor
    )

def execute_query(query,args=()):

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query,args)
            rows=cur.fetchall()
        return rows
    finally:
        conn.close()


def showpokemon(poke_type):
    query = "SELECT pokedex_number, name, type1 FROM Pokemon WHERE type1 = %s LIMIT 50;"
    return execute_query(query, (poke_type,))

def all_pokemon():
    query = "SELECT pokedex_number, name FROM Pokemon;"
    return query

def all_pokemon_stats():
    query = "SELECT pokedex_number, name, type1, hp, attack, defense, sp_attack, sp_defense FROM Pokemon;"
    return execute_query(query)

def show_damage_stats():
    query = "SELECT Pokemon.pokedex_number, name, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel, against_water FROM Pokemon JOIN Pokemon_Damage WHERE Pokemon.pokedex_number = Pokemon_Damage.pokedex_number;"
    
    return execute_query(query)

        
    
