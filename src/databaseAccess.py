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


def showpokemon(type):
    query = f"SELECT pokedex_number, name, type1 FROM Pokemon WHERE type1 = '{type}' LIMIT 10;"
    return execute_query(query)

