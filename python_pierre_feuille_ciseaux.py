# Créé par d, le 11/01/2023 en Python 3.7

import random

def verif(c,b,moves):
    if c == b :
        print("Egalité")
    ## 0 == Pierre
    ## 1 == Feuille
    ## 2 == Ciseaux
    elif c == 0 and b == 2 or c == 1 and b == 0 or c == 2 and b == 1:
        print("Joueur a gagné, il a utilisé ", moves[c], " et bot a utilisé ", moves[b])
    else:
        print("Joueur a perdu, il a utilisé ", moves[c], " et bot a utilisé ", moves[b])

moves = ["pierre","feuille","ciseaux"]

choix = int(input("Choississez un des trois choix parmis 0 : Pierre , 1 : Feuille , 2 : Ciseaux : "))

bot = random.randint(0,2)

verif(choix,bot,moves)