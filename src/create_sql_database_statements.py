# Code was created using CHATGPT
# The purpose of the code is to create statements from 


from pandas import *

df = read_csv("C://Users//sophi//OneDrive//Documents//pokemon.csv")

# Regenerate unique entries based on pokedex_number
unique_df = df.drop_duplicates(subset='pokedex_number')

# Define SQL create table statement
create_table_sql = """
CREATE TABLE Pokemon (
    pokedex_number INTEGER PRIMARY KEY,
    name TEXT,
    hp INTEGER,
    attack INTEGER,
    sp_attack INTEGER,
    defense INTEGER,
    sp_defense INTEGER,
    speed INTEGER,
    type1 TEXT,
    type2 TEXT,
    height_m2 REAL,
    weight_kg REAL,
    generation INTEGER,
    is_legendary BOOLEAN
);
"""



# Create insert statements for unique rows
insert_statements = []
for _, row in unique_df.iterrows():
    insert_sql = f"INSERT INTO Pokemon (pokedex_number, name, hp, attack, sp_attack, defense, sp_defense, speed, type1, type2, height_m2, weight_kg, generation, is_legendary) VALUES ({row['pokedex_number']}, '{row['name']}', {row['hp']}, {row['attack']}, {row['sp_attack']}, {row['defense']}, {row['sp_defense']}, {row['speed']}, '{row['type1']}', '{row['type2']}', {row['height_m2']}, {row['weight_kg']}, {row['generation']}, {bool(row['is_legendary'])});"

    insert_statements.append(insert_sql)

# Combine all SQL statements

print(create_table_sql)
for i in range(200):
    print(insert_statements[i])

