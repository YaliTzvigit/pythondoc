

# EXTRAIRE LES DONNEES / LIRE 

import pandas as pd

# pyplot de matplotlib 

import matplotlib.pyplot as plt

data = pd.read_csv("datax.csv", header=0, sep=",")

# afficher les premieres lignes 


print(data)  # il faut savoir simplement que : data.head() affiche > 5 premiers lignes de (0-4) et data >
                    # affiche toutes les lignes .... 




 # supprimer les 'NaN' par dropna() cette fonction axis=0 (toutles les NaN supprimés)

data.dropna(axis=0, inplace=True)

print(data)

 # Lister les types de données  : info()

print(data.info()) 

# convertir object en -> float64 pour les calculer 

data["Average_Pulse"] = data['Average_Pulse'].astype(float)
data["Max_Pulse"] = data['Max_Pulse'].astype(float)


print(data.info())


# Analysons les données maintznant : 

print(data.describe())

""" LES PERCENTILES x et(100-x)"""

import numpy as np

Max_Pulse = data["Max_Pulse"]

# 10% 

percent = np.percentile(Max_Pulse, 10)

# Afficher le percentile
print("Le percentiel 10 est de ", percent)

# afficher les ecarts-types (std)

std = np.std(data)

print(std) # sort les ecart-types

# Deduire le coeff de variation : 

cvar  = np.std(data) / np.mean(data)
print (cvar)

 # Deduire la variance avec (var) :

variance_full = np.var(data)

print(variance_full)




