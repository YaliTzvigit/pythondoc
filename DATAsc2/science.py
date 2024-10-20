
# extraire les datas 

import pandas as pd 

datas = pd.read_csv("paris_stocks.csv", header=0, sep=";")

# affiche , puisque le sep > ";"

print(datas)

 # nettoyer les données 

datas.dropna(axis=0, inplace=True)

print(datas)

 # extraire les deux premieres lignes
 # fsligne pour first-second lignes
fsligne = datas.iloc[:4]

print(fsligne)
