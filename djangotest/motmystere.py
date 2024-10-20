

# ecrire un programme en python qui permet a l'uitlisateur de trouver le mot mystere
# il doit deviner un mot 
# Le joueur possede 7 vies 
# On lui demande une lettre à chaque tour, si la lettre se troubve dans le mot alors ,
# on l'affiche , sinon il perd une vie, la parite s'arrete quand le joueur n'a plus de vie, ou si il a trouvé le mot mystere


nb_vies = 7
mot_mystere  = "python"

mot_public = '_' * len(mot_mystere)

while nb_vies > 0 and mot_mystere != mot_public:
    lettre = input('Entrez une lettre : ')

    
    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
    else:
        nb_vies -= 1
        
    if mot_public == mot_mystere:
        print("Vous avez gagné ! Le mot mystere est :", mot_mystere)
    elif nb_vies == 0:
        print(" Vous avez perdu !")
    else:
        print("Vous avez ", nb_vies) 
        print(" le mot est", mot_public)



