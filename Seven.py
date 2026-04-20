from random import randint
from itertools import combinations
import tkinter as tk

def menu():
    """Affiche une fenêtre pour que l'utilisateur choisisse le niveau de difficulté."""
    # Variable pour stocker le nombre de vies
    vies = [0]  # Liste mutable pour retourner la valeur

    def niveau_choisi(niveau):
        # Assigner le nombre de vies en fonction du niveau choisi
        if niveau == "Facile":
            vies[0] = 10
        elif niveau == "Normal":
            vies[0] = 7
        elif niveau == "Difficile":
            vies[0] = 4
        # Ferme la fenêtre après avoir choisi un niveau
        root.destroy()

    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Choisir le niveau")
    root.geometry("300x200")

    # Instructions
    label = tk.Label(root, text="Choisissez la difficulté du jeu :")
    label.pack(pady=10)

    # Création des boutons pour chaque niveau
    btn_facile = tk.Button(root, text="Facile (10 vies)", width=20, bg='green',
                           command=lambda: niveau_choisi("Facile"))
    btn_facile.pack(pady=5)

    btn_normal = tk.Button(root, text="Normal (7 vies)", width=20, bg='yellow',
                           command=lambda: niveau_choisi("Normal"))
    btn_normal.pack(pady=5)

    btn_difficile = tk.Button(root, text="Difficile (4 vies)", width=20, bg= 'red',
                              command=lambda: niveau_choisi("Difficile"))
    btn_difficile.pack(pady=5)

    # Boucle principale de Tkinter
    root.mainloop()

    # Retourne le nombre de vies choisi
    return vies[0]

# Initialisation des vies
vies = menu()
vies_init = vies

def grille():
    """Génère une grille de jeu avec des valeurs aléatoires entre 1 et 6.

    Returns:
        list: Une matrice 5x10 contenant des nombres aléatoires entre 1 et 6.
    """
    return [[randint(1,6) for _ in range(10)] for _ in range(5)]

# Création de la grille de jeu
grille_jeu = grille()

def lancer_new_des():
    """Génère deux nouveaux dés aléatoires.

    Returns:
        list: Une liste contenant deux nombres entre 1 et 6.
    """
    return [randint(1,6), randint(1,6)]

# Création des premiers dés supplémenaires
nouveaux2des = lancer_new_des()

def affichage():
    """Affiche l'état actuel du jeu, y compris le score, la grille et les vies."""
    print("\nScore : " + str(score)+"\n")

    # Affichage des vies sous forme de cœurs ♥ (pleines) et ♡ (perdues)
    coeur = "♥ " * vies + "♡ " * (vies_init - vies)

    nb = 64     # Code ASCII pour A (65), utilisé pour afficher les lettres A à E

    for liste in grille_jeu:
        nb += 1
        print("\t".join(str(x) if x != "" else "-" for x in liste[:9])+
                  "  |  "+chr(nb)+" → "+ str(liste[9]))

    # Ajustement du positionnement des dés en fonction du niveau
    if vies_init == 7:
        print("\nVies : " + str(coeur) + "                 F → "+str(nouveaux2des[0]) + "\n                                      G → "+ str(nouveaux2des[1])+"\n")
    if vies_init == 10:
        print("\nVies : " + str(coeur) + "           F → "+str(nouveaux2des[0]) + "\n                                      G → "+ str(nouveaux2des[1])+"\n")
    if vies_init == 4:
        print("\nVies : " + str(coeur) + "                       F → "+str(nouveaux2des[0]) + "\n                                      G → "+ str(nouveaux2des[1])+"\n")


def designe_last_elem(l):
    """Retourne la valeur du dé correspondant à la lettre choisie par le joueur.

    Args:
        l (str): Lettre choisie par le joueur (A-G, F, G ou 0).

    Returns:
        int: Valeur du dé ou 99 si invalide.
    """
    if l == 0:
        return 0
    if l == "F":
        if nouveaux2des[0] == "-":
            return 99
        return nouveaux2des[0]
    if l == "G" :
        if nouveaux2des[1] == "-":
            return 99
        return nouveaux2des[1]
    if l in "ABCDE":
        if grille_jeu[ord(l)-65][-1] == "":
            return 99
        return grille_jeu[ord(l)-65][-1]

def additions_des(i):
    """Vérifie si la somme des dés sélectionnés est égale à 7.

    Args:
        i (str): Combinaison de lettres choisies par le joueur.

    Returns:
        bool: True si la somme est 7, False sinon.
    """
    somme = 0
    if i == "V":
        return True
    for elem in i:
        somme += designe_last_elem(elem)
    if somme == 7:
        return True
    return False


def verifier_additions_des():
    """Vérifie s'il reste des combinaisons possibles qui donnent 7.

    Returns:
        bool: True s'il reste des combinaisons valides, False sinon.
    """
    compteur = 0
    for elem in liste_combo:
        if additions_des(elem):
                compteur += 1
    if compteur == 0 and vies == 0:
        return False
    return True

# Génération de toutes les combinaisons possibles de 2 à 7 lettres parmi A-G
comb = []
for i in range(2,8):
    comb.append(list(combinations("ABCDEFG", i)))
liste_combo = []
for i in range(len(comb)):
    for elem in comb[i]:
        liste_combo.append(''.join(elem))

def combinaisons(p):
    """Vérifie si la combinaison choisie est valide.

    Args:
        p (str): Combinaison de lettres choisies.

    Returns:
        bool: True si la combinaison est valide, False sinon.
    """
    if p in liste_combo or p == "V":
        return True
    print("La proposition donnée n'existe pas ou n'est pas possible")
    return False

# Initialisation du score
score = 0

# Initialisation du nombre de bonus déjà ajouté
bonus_ajoute = 0

def bonus_lignes_vides():
    """Calcule le bonus en fonction du nombre de lignes complètement vides.

    Returns:
        int: Le bonus à ajouter au score.
    """
    global bonus_ajoute # Évite l'erreur UnboundLocalError

    lignes_vides = 0

    # Vérifie si une ligne est vide
    for ligne in grille_jeu:
        est_vide = True
        for cell in ligne:
            if cell != '':
                est_vide = False

        if est_vide:
            lignes_vides += 1

    # On ajoute le bonus correspondant au nombre de lignes vides, bonus_ajoute permet d'ajouter le bonus une seule fois
    if lignes_vides == 5 and bonus_ajoute < 5:
        bonus_ajoute += 1
        return 100
    elif lignes_vides == 4 and bonus_ajoute < 4:
        bonus_ajoute += 1
        return 75
    elif lignes_vides == 3 and bonus_ajoute < 3:
        bonus_ajoute += 1
        return 50
    elif lignes_vides == 2 and bonus_ajoute < 2:
        bonus_ajoute += 1
        return 30
    elif lignes_vides == 1 and bonus_ajoute < 1:
        bonus_ajoute += 1
        return 15
    return 0

def jeu():
    """Gère le déroulement du jeu en exécutant les différentes étapes de vérification et d'affichage."""
    global nouveaux2des, score, vies    # Évite l'erreur UnboundLocalError

    affichage()

    while vies >= 0 :

        lettre_joueur = input("Choisir une combinaison entre A et G ou V :").upper()
        lettre_joueur = "".join(sorted(lettre_joueur))  # Trie alphabétiquement l'entrée


        # Vérifier si des combinaisons sont encore possibles
        if verifier_additions_des():

            # Vérifier si la combinaison est valide
            while combinaisons(lettre_joueur) == False:
                lettre_joueur = input("Choisir une combinaison entre A et G ou V :").upper()
                lettre_joueur = "".join(sorted(lettre_joueur))


            # Vérifier si la somme des dés est égale à 7
            while additions_des(lettre_joueur) == False:
                print("La somme ne fait pas 7 ou mauvaise saisie. Réessayez")
                lettre_joueur = input("Choisir une combinaison entre A et G ou V :").upper()
                lettre_joueur = "".join(sorted(lettre_joueur))

            if lettre_joueur == "V" :
                if vies > 0:
                    vies -= 1
                    nouveaux2des = lancer_new_des()
                else:
                    print("Il n'y a plus de vies disponible")


            # Mise à jour du score
            if lettre_joueur != "V":
                if len(lettre_joueur) == 2:
                        score += 7
                if len(lettre_joueur) == 3:
                    score += 15
                if len(lettre_joueur) == 4:
                    score += 30
                if len(lettre_joueur) == 5:
                    score += 50
                if len(lettre_joueur) == 6:
                    score += 75
                if len(lettre_joueur) == 7:
                    score += 100


            if "F" in lettre_joueur :               #
                nouveaux2des[0] = '-'               #
                                                    #
            if "G" in lettre_joueur :               #
                nouveaux2des[1] = '-'               #
                                                    #
            if nouveaux2des == ['-', '-']:          #
                nouveaux2des = lancer_new_des()     #
                                                    #
            if "A" in lettre_joueur :               #
                grille_jeu[0].pop(-1)               #
                grille_jeu[0].insert(0, "")         #
            if "B" in lettre_joueur :               #           Retire les dés une fois utilisés
                grille_jeu[1].pop(-1)               #
                grille_jeu[1].insert(0, "")         #
            if "C" in lettre_joueur :               #
                grille_jeu[2].pop(-1)               #
                grille_jeu[2].insert(0, "")         #
            if "D" in lettre_joueur :               #
                grille_jeu[3].pop(-1)               #
                grille_jeu[3].insert(0, "")         #
            if "E" in lettre_joueur :               #
                grille_jeu[4].pop(-1)               #
                grille_jeu[4].insert(0, "")         #

            score += bonus_lignes_vides()

            # Affichage du jeu après chaque tour
            affichage()


        # Si on a plus de vies et qu'il n'y a plus de possibilités de jouer, le jeu s'arrête
        if not verifier_additions_des() and vies == 0:
            print("Plus de combinaisons possibles. Score : {}".format(score))
            break


#   Lancement automatique du jeu
jeu()