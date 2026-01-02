import pandas as pd

df =pd.read_csv("pokemon.csv",index_col="name")

# pokemon= input("Enter a pokemon name: ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")

fast_pokemon= df[df["speed"] >=80 ] 
attacking_pokemon=df[df["attack"] >=100 ] 
water_pokemon=df[(df["type_1"]=="Fire") & (df["type_2"]=="Flying") ] 
#print(attacking_pokemon)
#print (fast_pokemon)
print(water_pokemon)

