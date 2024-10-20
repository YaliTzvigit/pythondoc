

# Autre recuperation de data : 


# deduis une structure >

class strExtr : 
    def __init__(self, y):
        self._nom = y[0]
        self._adresse = y[1]
        self._identifiant = y[2]
        self._ibn = y[3]



# nom du fichier : 
        

filename = r"C:\tmp\PytData.csv"


# supp les en tetes: 

lignCount = 0

extra = {}

with open(filename) as f:
    for line in f:
        if (lignCount >= 1): # ignorer la 1ere ligne
            y = line.replace(',', '').split(";")
            if not '.' in y:
                extra[y[3]] = strExtr(y)
                lignCount += 1
            


print(extra['KOD']._opp)


