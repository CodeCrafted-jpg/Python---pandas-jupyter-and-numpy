import pandas as pd

df =pd.read_csv("pokemon.csv",index_col="name")
try:
 

    # 2. Get user input
    user_query = input("Enter a Pokémon name: ").strip()

    # 3. Perform a case-insensitive search
    # We compare the lowercased 'name' column to the lowercased user input
    match = df[df['name']]

    if not match.empty:
        # Extract data from the first (and only) row found
        name = match.iloc[0]['name']
        type1 = match.iloc[0]['type_1']
        type2 = match.iloc[0]['type_2']

        # 4. Display the result cleanly
        if pd.isna(type2):
            print(f"{name} is a pure {type1} type.")
        else:
            print(f"{name} is a dual {type1}/{type2} type.")
    else:
        print(f"Sorry, '{user_query}' was not found in the original 151 Pokémon.")

except FileNotFoundError:
    print(f"Error: Could not find 'pokemon.csv'") 