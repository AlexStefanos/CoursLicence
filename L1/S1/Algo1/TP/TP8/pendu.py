# -*- coding: utf-8 -*-

from donnees import *
from random import choice
#Fonction permettant de récupérer une lettre tapée par l’utilisateur
def recup_lettre():
    """ None --> Str
    Cette fonction récupère une lettre saisie par
    l’utilisateur."""
    lettre = input("Tapez une lettre: ")
    lettre = lettre.lower()
    if len(lettre)>1 or not lettre.isalpha():
        print("Vous n’avez pas saisi une lettre valide.")
        return recup_lettre()
    else:
        return lettre
# Fonction permettant de choisir un mot
def choisir_mot():
    """None --> Str
    Cette fonction renvoie le mot choisi dans la liste des mots
    liste_mots."""
    return choice(liste_mots)
#Fonction permettant d’afficher uniquement les lettres déjà trouvées d’un mot
def recup_mot_masque(mot_complet, lettres_trouvees):
    """Str x List --> Str
    Retourne le mot d’origine avec des * remplaçant les lettres que l’on
    n’a pas encore trouvées."""
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees or lettre == "-":
            mot_masque = mot_masque + lettre
        else:
            mot_masque = mot_masque + "*"
            return mot_masque
    #Programme principal
mot_a_trouver = choisir_mot()
lettres_trouvees = []
mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
nb_chances = nb_coups
while mot_a_trouver!=mot_trouve and nb_chances>0:
    print("Mot à trouver", mot_trouve,"(encore", nb_chances, "chance(s))")
    lettre = recup_lettre()
    if lettre in lettres_trouvees: # La lettre a déjà été choisie
        print("Vous avez déjà choisi cette lettre.")
    elif lettre in mot_a_trouver: # La lettre est dans le mot à trouver
        lettres_trouvees.append(lettre)
        print("Bien joué.")
    else:
        nb_chances = nb_chances - 1
        print("... non, cette lettre ne se trouve pas dans le mot...")
        mot_trouve = recup_mot_masque(mot_a_trouver, lettres_trouvees)
# A-t-on trouvé le mot ou nos chances sont-elles épuisées ?
if mot_a_trouver==mot_trouve:
    print("Félicitations ! Vous avez trouvé le mot", mot_a_trouver)
else:
    print("PENDU !!! Vous avez perdu. Le mot à trouver était", mot_a_trouver)
