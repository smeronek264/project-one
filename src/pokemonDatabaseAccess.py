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
    query = "SELECT pokedex_number, name, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel, against_water FROM Pokemon JOIN Pokemon_Damage WHERE Pokemon.pokedex_number = Pokemon_Damage.pokedex_number;"
    
    new_query = []
    for pokemon in query:
        effective_list = []
        if pokemon.against_bug == "Strong":
            effective_list.append("Bug")
        if pokemon.against_dark == "Strong":
            effective_list.append("Dark")
        if pokemon.against_dragon == "Strong":
            effective_list.append("Dragon")
        if pokemon.against_electric == "Strong":
            effective_list.append("Electric")
        if pokemon.against_fairy == "Strong":
            effective_list.append("Fairy")
        if pokemon.against_fight == "Strong":
            effective_list.append("Fight")
        if pokemon.against_fire == "Strong":
            effective_list.append("Fire")
        if pokemon.against_ghost == "Strong":
            effective_list.append("Ghost")
        if pokemon.against_grass == "Strong":
            effective_list.append("Grass")
        if pokemon.against_ground == "Strong":
            effective_list.append("Ground")
        if pokemon.against_ice == "Strong":
            effective_list.append("Ice")
        if pokemon.against_normal == "Strong":
            effective_list.append("Normal")
        if pokemon.against_poison == "Strong":
            effective_list.append("Poison")
        if pokemon.against_psychic == "Strong":
            effective_list.append("Psychic")
        if pokemon.against_rock == "Strong":
            effective_list.append("Rock")
        if pokemon.against_steel == "Strong":
            effective_list.append("Steel")
        if pokemon.against_water == "Strong":
            effective_list.append("Water")

        new_query.append({
            "pokedex_number": pokemon.get("pokedex_number"),
            "name": pokemon.get("name"),
            "effective_list": effective_list
        })

    return new_query

        
    
