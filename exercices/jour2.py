#==============================================================
# Les listes - Stocker plusieurs valeurs dans une variable
#==============================================================

#depense = ["loyer", "course", "transport", "abonnement", "loisirs", "netflix"]

#print(depense[0])
#print(depense[3])
#print(depense[4])
#print(depense[-1])


#depense.remove("netflix")
#depense.append("essence")

#print(f"le nombre d'élément de ma liste est de {len(depense)}")


#==============================================================
# Les boucles
#==============================================================

#print("Mes dépenses du mois")
#for i in depense:
 #   print(f"- {i}")

#montant = [200,600,900,5,450,780,3]
#total = 0
#for i in montant :
 #   total = total +i
  #  print(f"le montant du mois est {i} pour un montant cumulé total de {total}")

#print (f"\nLe montant final est de {total}€")



#__________ les boucles avec index__________
#print("\n ====Les liste numérotés====")
#for i, dep in enumerate(depense):
 #   print(f"{i+1}. {dep}")

#for i in range(5,0,-1):
 #   print (f"{i}...")
#print ("décollage!!!.")

#_____________Boucle sur deux listes parrallèle________________
#noms = ["loyer","course", "transport"]
#montants = [400,5200,6235]

#print("\n Dépenses détaillé par poste ")

#for nom, montant in zip(noms,montants):
 #   print(f"{nom} : {montant}€")

#==============================================================
# la boucle While  - Repeter tant que une condition est vrai
#==============================================================

print("============Ajouter des dépenses=================")
print ("\n Tape STOP pour arrêter")
depenses =[]

while True:
    saisie = input("Nom de la dépense:")
    if saisie == "STOP":
        break
    montant = float(input(f"Montant pour la dépense {saisie}:"))
    depenses.append({"nom": saisie,"montant":montant})
    print(f"✅ {saisie} ({montant}€) ajouté !\n")

print("============== Résumé=============")
total =0
for dep in depenses:
    print(f"- {dep['nom']} : {dep['montant']}€")
    total += dep['montant']

print(f"\n Le montant total des dépenses est de {total}€")
print (f"Le nombre de dépense réalisé sur le mois est de : {len(depenses)}.")


#__________ Liste de dictionnaire_____________

budget = [
    {"nom" : "Loyer", "montant": 800, "categorie": "Logement"},
    {"nom" : "Courses", "montant":300, "categorie": "Alimentation"},
    {"nom": "Métro", "montant":100, "categorie": "Transport"},
    {"nom": "Netflix", "montant":20, "categorie":"Divertissement"},
    {"nom": "Resto", "montant":300, "categorie": "Alimentation"},
]
print("\n =====Afficher toute mes dépenses==========")
for dep in budget:
    print(f"{dep['nom']:.<20} {dep['montant']:>6} [{dep['categorie']}]")

total_general =sum(dep['montant'] for dep in budget)
print(f"\n💰 Total général : {total_general}€")

# ═══════════════════════════════════════════
# LES FONCTIONS — Créer tes propres commandes
# ═══════════════════════════════════════════

def saluer( prenom):
    """Affiche un message de bienvenu"""
    print(f"\n Bonjour {prenom} et bienvenu au cours de français")

saluer ("Sarah")
saluer("Paul")
