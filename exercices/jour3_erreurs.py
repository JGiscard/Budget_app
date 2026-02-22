# ═══════════════════════════════════════════
# GESTION DES ERREURS — Empêcher le programme de crasher
# ═══════════════════════════════════════════

# Le problème : dans budget_v2, si l'utilisateur tape "abc"
# quand on demande un montant → float("abc") → CRASH !

# ─── Sans gestion d'erreur ───
# Décommente pour voir le crash :
# nombre = float(input("Entre un nombre : "))
# Si tu tapes "bonjour" → ValueError: could not convert string to float

# ─── Sans gestion d'erreur ───
# Décommente pour voir le crash :
# nombre = float(input("Entre un nombre : "))
# Si tu tapes "bonjour" → ValueError: could not convert string to float

# ─── Avec try/except ───
# print("=== Test 1 : gestion basique ===")
# try:
#     nombre = float(input("entre un nombre:"))
#     print(f"✅ Tu as entré : {nombre}")
# except ValueError:
#     print("❌ Ce n'est pas un nombre valide !")

    # ─── Boucle jusqu'à saisie valide ───
# from ast import IsNot
# from operator import truediv
# from zipfile import MAX_EXTRACT_VERSION


# print("\n=== Test 2 : redemander jusqu'à obtenir un nombre ===")
# while True:
#     try :
#         montant = float(input("Montant de la dépense (€) : "))
#         if montant <0 :
#             print("⚠️  Le montant ne peut pas être négatif !")
#             continue
#         break
#     except ValueError:
#         print("❌ Entre un nombre valide ! (ex: 42.50)")

# print(f"✅ Montant enregistré : {montant}€")

# # ─── Plusieurs types d'erreurs ───
# print("\n=== Test 3 : différents types d'erreurs ===")
# try :
#     with open ("fichier_inexistant.txt","r") as f:
#         contenu = f.read()
# except FileNotFoundError:
#     print("❌ Ce fichier n'existe pas !")

# # Erreur de division
# try:
#     resultat = 100/0
# except ZeroDivisionError:
#     print("Impossible de faire un division par 0.")

# # Erreur de clé dans un dictionnaire
# try : 
#     depenses = {"nom": "Loyer", "montant": 400}
#     print(depenses["non"])
# except KeyError:
#     print("❌ Cette clé n'existe pas dans le dictionnaire !")

# ─── Le bloc complet : try/except/else/finally ───
# print("\n=== Test 4 : bloc complet ===")
# try:
#     nombre = float(input("entre un nombre:"))
# except ValueError:
#      print("❌ Pas un nombre !")
# else:
#     print(f"✅ Bravo, {nombre} est valide !")
#     # else s'exécute SEULEMENT si try a réussi
# finally:
#     print("🏁 Ce message s'affiche TOUJOURS, erreur ou pas.")
    # finally s'exécute dans TOUS les cas

def demander_nombre (message, minimum = None, maximum = None):
    """Demande un nombre à l'utilisateur avec validation"""
    while True:
        try:
            print(message)
            valeur = float(input())
            if minimum is not None and valeur < minimum:
                print(f"Le nombre entré doit être supérieur à {minimum}")
                continue
            elif maximum is not None and valeur > maximum:
                print(f"Le nombre entré doit être inférieur à {maximum}")
                continue
            return valeur
        except ValueError:
            print(f"Ceci n'est pas nombre. Pourrais tu renter ton {message} s'il te plait ?")

print("\n=== Test des fonctions robustes ===")
age = demander_nombre("Ton âge : ", minimum=0, maximum=150)
print(f"Tu as {age} ans !")
