import pandas as pd

mods = pd.read_csv("Data Science\Mods.csv")

print(mods['#Mod_Name'])

print(mods[['#Mod_Name']])

print(mods[['#Mod_Name', '#Nexus_ID']])

print(mods[0:4])

print(mods[4:6])

print(mods.iloc[2])