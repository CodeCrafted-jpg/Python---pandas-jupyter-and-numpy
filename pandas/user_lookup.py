import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="name")

user_query = input("Enter a Pokémon name: ").strip().capitalize()

try:
   
    pokemon_data = df.loc[user_query]
    
    t1 = pokemon_data['type_1']
    t2 = pokemon_data['type_2']
    
    if pd.isna(t2):
        print(f"{user_query} is a pure {t1} type.")
    else:
        print(f"{user_query} is a dual {t1}/{t2} type.")
except KeyError:
    print(f"Could not find '{user_query}' in the index.")