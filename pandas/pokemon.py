import pandas as pd

df =pd.read_csv("pokemon.csv",index_col="name")

pokemon= input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")

     