import random

# Génération du prix à deviner
prix = random.randint(0, 2000)
#print("Prix (pour test) :", prix)

# --------- Fonction 1 : recherche par l'utilisateur ---------
def fctl(prix):
    essai = 0
    answer = -1

    while answer != prix:
        answer = int(input("Donnez un prix : "))
        essai += 1

        if answer > prix:
            print("moins")
        elif answer < prix:
            print("plus")

    print("Valeur à trouver :", prix, "| Nombre d'essais :", essai)


# --------- Fonction 2 : recherche automatique ---------
def fct2(prix):
    essai = 0
    debut = 0
    fin = 2000
    answer = -1

    while answer != prix:
        mil = (debut + fin) // 2
        answer = mil
        essai += 1

        print("Essai n°", essai, "- Valeur testée :", answer)

        if answer > prix:
            fin = mil - 1
        elif answer < prix:
            debut = mil + 1

    print("Trouvé en", essai, "essai(s)")


# Appels des fonctions
# fct2(prix)   # Recherche automatique
# fctl(prix)   # Décommenter pour jouer manuellement

