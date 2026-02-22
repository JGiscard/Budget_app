# ═══════════════════════════════════════════
# LES FICHIERS — Sauvegarder des données
# ═══════════════════════════════════════════

#============== Ecrire dans un fichier===============

# fichier = open("test.txt", "w")
# fichier.write("Bonjour \n")
# fichier.write("Ceci est mon premier fichier\n")
# fichier.write("Ligne 3 \n")
# fichier.close()

# print("✅ Fichier 'test.txt' créé !")

#================Lire un fichier==================

# fichier = open("test.txt","r")
# contenu = fichier.read()
# fichier.close()

# print("\n📖 Contenu du fichier :")
# print(contenu)

# #lire ligne par ligne
# fichier = open("test.txt","r")
# lignes = fichier.readlines()
# fichier.close()

# print("Ligne par ligne")
# for i, ligne in enumerate(lignes):
#     print(f"La ligne {(i+1)} est : {ligne.strip()}")

# ─── La méthode PROPRE : with (recommandée) ───
# Plus besoin de .close() → Python le fait automatiquement !

# with open("test.txt","w") as f:
#     f.write("Méthode propre ligne 1.\n")
#     f.write("Méthodeo propres ligne 2.\n")
#     f.write("Methode propre fin.")

# with open("test.txt","r") as f:
#     print("Aver la méthode with")
#     print(f.read())


# ═══════════════════════════════════════════
# JSON — Le format idéal pour sauvegarder des données structurées
# ═══════════════════════════════════════════

# Un fichier .txt c'est bien pour du texte simple
# Mais pour sauvegarder des LISTES et des DICTIONNAIRES ?
# → JSON ! (JavaScript Object Notation)
# C'est LE format universel d'échange de données

from ast import dump
import json

#----------------Nos données comme dans budget V2-------------------

donnees = {
    "revenus" : 200,
    "depenses": [
        {"nom" : "loyer","montant" : 700, "categorie" : "Logement"},
        {"nom": "Courses", "montant": 250, "categorie": "Alimentation"},
        {"nom": "Métro",   "montant": 75,  "categorie": "Transport"},
        {"nom": "Netflix", "montant": 15.99, "categorie": "Loisirs"},
    ]}

#-----------Sauvegarde en JSON---------------
with open("budget_data.json","w", encoding = "utf-8") as f:
    json.dump(donnees, f, ensure_ascii=False, indent=4)
    # json.dump()      → écrit le dictionnaire dans le fichier
    # ensure_ascii=False → garde les accents (é, è, ê...)
    # indent=4          → format lisible (pas tout sur une ligne)
print("✅ Données sauvegardées dans budget_data.json !")
print("→ Va ouvrir ce fichier dans Cursor pour voir à quoi ça ressemble\n")

# ─── CHARGER depuis un JSON ───
with open("budget_data.json","r",encoding="utf-8") as f:
    donnees_chargees  = json.load(f)
    # json.load() → lit le fichier et recrée le dictionnaire Python

print("📂 Données chargées :")
print(f"  Revenus : {donnees_chargees['revenus']}€")
print(f"  Nombre de dépenses : {len(donnees_chargees['depenses'])}")

# ─── Modifier et re-sauvegarder ───
# Ajoutons une dépense
nouvelle_depense = {"nom": "Essence", "montant": 60, "categorie": "Transport"}
donnees_chargees["depenses"].append(nouvelle_depense)

# Re-sauvegarde
with open("budget_data.json","w",encoding="utf-8") as f:
    json.dump(donnees_chargees,f,ensure_ascii=False,indent=4)

print("\n✅ Nouvelle dépense ajoutée et sauvegardée !")
print("→ Réouvre budget_data.json pour voir le changement")

# ─── Créer des fonctions réutilisables ───
def sauvegarder(donnees, fichier="budget_data.json"):
    """Sauvegarde les données dans un fichier JSON"""
    with open(fichier,"w",encoding='utf-8') as f:
        json.dump(donnees,f,ensure_ascii=False,indent =4)
        print(f"💾 Sauvegardé dans {fichier}")

def charger(fichier="budget_data.json"):
     """Charge les données depuis un fichier JSON"""
     with open(fichier,"r",encoding="utf-8") as f:
        donnees = json.load(f)
        return donnees

# Test des fonctions
mes_donnees = charger()
print(f"\n📂 Chargé : {len(mes_donnees['depenses'])} dépenses")
mes_donnees["depenses"].append({
    "nom": "Téléphone",
    "montant": 20,
    "categorie": "Autre"
})
sauvegarder(mes_donnees)