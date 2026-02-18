#================= Exercice 1 : Les variables ================
from re import A


#prénom = "alex"
#age = 28
#salaire = 52.01
#estEtudiant = False

# Afficher les variables
#print (prénom)
#print (age)
#print (salaire)
#print(estEtudiant)

#Afficher le type de variable
#print(type(prénom))
#print(type(age))
#print(type(salaire))
#print(type(estEtudiant))

# Changer une valeur
#age= "Bonjour paul"

#print(type(age))


#================= Exercice 2 : Les Opérations==============
#revenus = 5000
#loyer = 500
#course = 600
#transport = 80
#loisirs = 60

#calcul
#TotalDepense = loyer + course + transport + loisirs
#Epargne = revenus - TotalDepense

#print("=============Mon Budget============")
#print(f"Revenus : {revenus}€")
#print(f"Dépense : {TotalDepense}€")
#print(f"Epargne : {Epargne}€")

#pourcentagedepense = TotalDepense*100/revenus

#print(f"tu dépense en moyenne {pourcentagedepense}% de tes revenus par mois")

#print ("===================Exercice 3 : Interagir avec l'utilisateur================")

#print("Calculateur de budget personnel")
#print()


def demander_nombre(message):
    """Demande un nombre à l'utilisateur jusqu'à ce qu'il entre une valeur valide."""
    while True:
        try:
            valeur = float(input(message))
            if valeur < 0:
                print("⚠️  Entrez un nombre positif.")
                continue
            return valeur
        except ValueError:
            print("⚠️  Erreur : vous devez entrer un nombre (ex: 1500 ou 99.50). Réessayez.\n")


# Demander à l'utilisateur de saisir ses revenus et dépenses

#Epargne = revenus - (loyer + course + transport)

#print()
#print(f"Votre epargne mensuelle est de {Epargne}€")

# ================== Exercice 4 : Le mini programme================

print("╔═══════════════════════════════════════════════════════════════════════╗")
print("║            💰 Calculateur de budget personnel 💰                     ║")
print("╚═══════════════════════════════════════════════════════════════════════╝")

revenus = demander_nombre("Entrez vos revenus mensuels : ")
print()

print("🏠 Dépenses :")

loyer = demander_nombre("Entrez votre loyer mensuel : ")
print()
course = demander_nombre("Entrez vos dépenses de courses : ")
print()
transport = demander_nombre("Entrez vos dépenses de transport : ")
print()
abonnement = demander_nombre("Entrez vos dépenses d'abonnement : ")
print()
TotalDepense = loyer + course + transport + abonnement
Epargne = revenus - TotalDepense
print()
print("="*50)
print("Bilan du mois :")
print("="*50)
print(f"Revenus : {revenus}€")
print(f"Dépenses : {TotalDepense}€")
print("________________________________________")
print(f"Epargne : {Epargne}€")
print("="*50)

if Epargne > 1000:
    print("🎉 Félicitations ! Vous avez atteint votre objectif d'épargne mensuelle.")
elif Epargne > 500:
     print("correct, mais reste prudent ")
elif Epargne > 0:
    print ("Budget équilibré, attention à vos dépenses.")
else:
    print("💸 Vous êtes en déficit, attention à vos dépenses.")

depensedict = {"Loyer": loyer, "Courses": course, "Transport": transport, "Abonnement": abonnement}

plusgrosse = max(depensedict, key=depensedict.get)  # catégorie dont le montant est le plus élevé
print(f"\nLa dépense la plus importante est {plusgrosse} : {depensedict[plusgrosse]}€")