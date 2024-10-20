

import random

def melanger_lettres(mot):
    lettres = list(mot)
    random.shuffle(lettres)
    return ''.join(lettres)

def jeu_de_mots():
    # Liste de mots possibles
    mots_possibles = ['pome', 'tabe', 'chat', 'lion', 'jour', 'soleil']
    
    # Choisir un mot aléatoire de 4 lettres parmi la liste
    mot_a_deviner = random.choice([mot for mot in mots_possibles if len(mot) == 4])

    # Mélanger les lettres du mot
    lettres_melangees = melanger_lettres(mot_a_deviner)
    
    print("Bienvenue dans le jeu de mots!")
    print(f"Trouvez le mot correct à partir de ces lettres : {lettres_melangees}")
    
    essais = 0
    
    while True:
        # Demander à l'utilisateur de deviner le mot
        devinette = input("Entrez votre devinette : ").strip().lower()
        essais += 1
        
        # Vérifier si la devinette est correcte
        if devinette == mot_a_deviner:
            print(f"Bravo! Vous avez trouvé le mot '{mot_a_deviner}' en {essais} essais.")
            break
        else:
            print("C'est incorrect, essayez encore!")

# Lancer le jeu
jeu_de_mots()
