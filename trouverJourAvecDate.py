# coding: utf-8

# variables
# dictionnaire contenant les mois de l'année et les points leurs étant associés
mois = {
    "Janvier": 0,
    "Février": 3,
    "Mars": 3,
    "Avril": 6,
    "Mai": 1,
    "Juin": 4,
    "Juillet": 6,
    "Août": 2,
    "Septembre": 5,
    "Octobre": 0,
    "Novembre": 3,
    "Décembre": 5
}
# dictionnaire contenant les siècles et les points leurs étant associés
siecle = {
    "annees 1600": 6,
    "annees 1700": 4,
    "annees 1800": 2,
    "annees 1900": 0,
    "annees 2000": 6,
    "annees 2100": 4
}
# dictionnaire contenant les jours de la semaine et leurs indices
jourSemaine = {
    0: "Dimanche",
    1: "Lundi",
    2: "Mardi",
    3: "Mercredi",
    4: "Jeudi",
    5: "Vendredi",
    6: "Samedi"
}

# variable contenant la date saisie par l'utlisateur sous forme de chaine de caractère : "jj/mm/aaaa"
dateSaisieParUtilisateur = input("saisir la date sous forme jj/mm/aaaa : ")
# contient le total nous permmettant de deviner le jour de la semaine recherché
total = 0


# fonctions
# "jour" : correspond au jour saisie par l'utilisateur de 1 à 31
#  "mois" : correspond au mois saisie par l'utilisateur sous forme janvier, février...
# "annee" : correspond a l'année saisie par l'utilisateur, utilisé pour le calcul de l'année bissextile
# "anneeDeb" : correspond au siecle de l'annee ex : 16 / 17 / 18 / 19 / 20
# "anneeFin" : correspond au deux derniers caractères de l'annee saisie par l'utilisateur
# permet de fragmenter la chaine de caractères saisie par l'utilisateur pour mettre les valeurs en adequation avec les variables
def convertir_date_utilisateur(chaineSaisie):
    dateSaisie = chaineSaisie.split("/")
    jourSaisie = dateSaisie[0]
    moisSaisie = dateSaisie[1]
    anneeSaisie = dateSaisie[2]

    # permet d'assigner le nom du mois à la variable mois
    indice = 1
    for cle in mois.keys():
        if indice == int(moisSaisie):
            moisSaisie = cle
            break
        indice += 1

    # permet de mettre les deux premiers caractères de l'annee saisie par l'utilisateur dans la variable anneeDeb
    anneeDebSaisie = dateSaisie[2][0:2]
    # permet de mettre les deux derniers caractères de l'annee saisie par l'utilisateur dans la variable anneeFin
    anneeFinSaisie = dateSaisie[2][2:4]
    return int(jourSaisie), moisSaisie, int(anneeSaisie), int(anneeDebSaisie), int(anneeFinSaisie)


# calcul : https://fr.wikihow.com/calculer-les-ann%C3%A9es-bissextiles
# permet de savoir si l'année est bissextile et retourne True si c'est le cas ou False
def annee_est_bissextile(anneeSaisie):
    if anneeSaisie % 4 == 0:
        if anneeSaisie % 100 != 0:
            return True
        else:
            if anneeSaisie % 400 == 0:
                return True
            else:
                return False

        return False
    else:
        return False


# fonction qui retourne le jour de la semaine
# On garde les deux derniers chiffres de l'année en question ex ->(1947 → 47)
# On ajoute 1/4 de ce nombre en ignorant les restes (47/4 = 11, reste 3 ignoré)
# On ajoute la journée du mois
# Selon le mois on ajoute la valeur lui corespondant dans le dictionnaire "mois"
# Si l'année est bissextile et le mois est janvier ou février, on ôte 1
# Selon le siècle on ajoute la valeur lui corespondant dans le dictionnaire "siècle"
# On divise la somme par 7 et on garde le reste
# Le reste représente le jour de la semaine recherché le dictionnaire "jourSemaine"
def calcul_jour(dateUtilisateur):
    # on appel la méthode "convertir_date_utilisateur" pour attribuer les valeurs aux variables
    jour, moisSaisie, annee, anneeDeb, anneeFin = convertir_date_utilisateur(dateUtilisateur)
    total = anneeFin + (int(anneeFin) // 4) + jour + mois.get(moisSaisie)
    if annee_est_bissextile(annee) and moisSaisie == "janvier" and moisSaisie == "février":
        total -= 1
    total += siecle.get("annees " + str(anneeDeb) + "00")
    total %= 7
    return jourSemaine.get(total)


print(calcul_jour(dateSaisieParUtilisateur))
