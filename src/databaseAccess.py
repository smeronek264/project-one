# import pymysql
# import pymysql.cursors
# import creds
# import boto3

# def get_conn():

#     return pymysql.connect(
#         host=creds.host,
#         user=creds.user,
#         password=creds.password,
#         db=creds.db,
#         cursorclass=pymysql.cursors.DictCursor
#     )

# def execute_query(query,args=()):

#     conn = get_conn()
#     try:
#         with conn.cursor() as cur:
#             cur.execute(query,args)
#             rows=cur.fetchall()
#         return rows
#     finally:
#         conn.close()


# def showpokemon(poke_type):
#     query = "SELECT pokedex_number, name, type1 FROM Pokemon WHERE type1 = %s LIMIT 10;"
#     return execute_query(query, (poke_type,))

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


def show_country():
    query = "SELECT Name, Continent, Region, Population FROM country LIMIT 20;"
    return execute_query(query)



