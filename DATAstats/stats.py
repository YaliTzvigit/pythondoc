

import pandas as pd

datab = pd.read_csv("stocksdata.csv", header=0, sep=";")

print(datab)

# supprimer 'NaN' 

datab.dropna(inplace=True,axis=0)

print(datab)

# Convertir  les données en float : object > float 

datab["Closing_Price"] = datab['Closing_Price'].astype(float)

print(datab.info())

# FULL affichage :> 

print(datab.describe())


""" LES PERCENTILES """

import numpy as np 

low_price = datab["low_price"]

percentilet = np.percentile(low_price, 10)

print(percentilet)

