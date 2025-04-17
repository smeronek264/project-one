import pymysql
import pymysql.cursors
import creds
import boto3

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

