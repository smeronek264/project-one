# This code was to create SQL queries to enter in the pokemon damage data 
# It will show how different types will do against the pokemon
# THIS WAS WRITTEN USING CHATGPT

from pandas import *

# Load CSV
df = read_csv("data/pokemon_weakness.csv")

# Drop duplicates by pokedex_number
unique_df = df.drop_duplicates(subset='pokedex_number')

# CREATE TABLE with all columns as TEXT (except pokedex_number)
create_table_sql = """
CREATE TABLE Pokemon_Damage (
    pokedex_number INTEGER PRIMARY KEY,
    against_bug TEXT,
    against_dark TEXT,
    against_dragon TEXT,
    against_electric TEXT,
    against_fairy TEXT,
    against_fight TEXT,
    against_fire TEXT,
    against_ghost TEXT,
    against_grass TEXT,
    against_ground TEXT,
    against_ice TEXT,
    against_normal TEXT,
    against_poison TEXT,
    against_psychic TEXT,
    against_rock TEXT,
    against_steel TEXT,
    against_water TEXT
);
"""

# Generate INSERT statements with values as text
insert_statements = [
    f"INSERT INTO Pokemon_Damage (pokedex_number, against_bug, against_dark, against_dragon, against_electric, against_fairy, against_fight, against_fire, against_ghost, against_grass, against_ground, against_ice, against_normal, against_poison, against_psychic, against_rock, against_steel, against_water) VALUES ({row['pokedex_number']}, " +
    ", ".join([f"'{('Strong' if row[col] > 1 else 'Weak' if row[col] < 1 else 'Standard')}'" for col in [
        'against_bug', 'against_dark', 'against_dragon', 'against_electric', 'against_fairy',
        'against_fight', 'against_fire', 'against_ghost', 'against_grass', 'against_ground',
        'against_ice', 'against_normal', 'against_poison', 'against_psychic',
        'against_rock', 'against_steel', 'against_water'
    ]]) +
    ");"
    for _, row in unique_df.iterrows()
]

# Output SQL
# print(create_table_sql)
for i in range(101, 200):
    print(insert_statements[i])
