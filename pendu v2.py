import unidecode
from random import randint

mots = []

with open('liste_francais.txt') as f:
    mots = f.readlines()


def mot_mystere():
    numero_random = randint(0, len(mots)-1)
    mot_mystere = unidecode.unidecode(mots[numero_random])
    mot_mystere_liste = []
    mot_mystere_guess = []
    for i in range(0, len(mot_mystere)-1):
        mot_mystere_liste.append(mot_mystere[i].upper())
        mot_mystere_guess.append("_")
    # print(mot_mystere, mot_mystere_liste)
    return mot_mystere_liste, mot_mystere_guess, mot_mystere
        
def deviner(lettre, mot_mystere_liste, mot_mystere_guess, logs, essais):
    if lettre not in logs:
        if lettre in mot_mystere_liste:
            for i in range(0, len(mot_mystere_liste)):
                if mot_mystere_liste[i] == lettre:
                    mot_mystere_guess[i] = lettre
            print("La lettre " + lettre + "est bien dans le mot mystere.")
        else:
            essais -= 1
            print("La lettre " + lettre + " n'est pas dans le mot mystere.")
    else:
        print("Vous avez deja saisi la lettre", lettre)
    return mot_mystere_guess, essais

def commencer():
    oui = ["oui", "OUI", "yes", "YES"]
    non = ["non", "NON", "no", "NO"]
    commencer_ok = False
    while commencer_ok == False:
        commencer = input("Voulez vous commencer une partie ? (oui/non) ")
        if commencer in oui:
            jouer = True
            commencer_ok = True
        elif commencer in non:
            jouer = False
            commencer_ok = True
        else:
            print("Veuillez saisir oui ou non")
    return jouer

def affichage(mot_mystere_guess, essais):
    print(" ".join(mot_mystere_guess))
    if essais == 0:
        print("Vous avez perdu")
    else:
        print("Il vous reste", essais, "essais")
    return

def continuer(gagner):
    oui = ["oui", "OUI", "yes", "YES"]
    non = ["non", "NON", "no", "NO"]
    continuer_ok = False
    keep_playing = bool
    while continuer_ok == False:
        continuer = input("Voulez-vous continuer la partie ? (oui/non) ")
        if continuer in oui:
            keep_playing = True
            continuer_ok = True
        elif continuer in non:
            keep_playing = False
            continuer_ok = True
            gagner = True
            print("Merci d'avoir joue.")
        else:
            print("Veuillez saisir oui ou non")
    return keep_playing, gagner

def verifier(mot_mystere_liste, mot_mystere_guess, gagner, keep_playing, essais):
    if mot_mystere_liste == mot_mystere_guess:
        gagner = True
        keep_playing = False
        print("Bravo ! Vous avez gagne")
    elif essais == 0:
        gagner = True
        keep_playing = False
    return gagner, keep_playing

def lettre_input():
    lettre = ""
    lettre_ok = False
    while lettre_ok == False:
        lettre = unidecode.unidecode(input("Veuillez saisir une lettre: ").upper())
        if len(lettre) == 1:
            lettre_ok = True
        else:
            print("Veuillez ne saisir qu'une seule lettre")
    return lettre

def pendu():
    jouer = commencer()
    while jouer == True:
        mot_mystere_liste, mot_mystere_guess, mot = mot_mystere()
        keep_playing = True
        essais = 11
        logs = ""
        affichage(mot_mystere_guess, essais)
        gagner = False
        while gagner == False:
            while keep_playing == True:
                lettre = lettre_input()
                mot_mystere_guess, essais = deviner(lettre, mot_mystere_liste, mot_mystere_guess, logs, essais)
                logs += lettre
                affichage(mot_mystere_guess, essais)
                gagner, keep_playing = verifier(mot_mystere_liste, mot_mystere_guess, gagner, keep_playing,essais)
                if gagner == False:
                    keep_playing, gagner = continuer(gagner)
        print("Le mot etait:", mot)
        jouer = commencer()
    return