# ═══════════════════════════════════════════
# 🏦 BUDGET APP v3 — Sauvegarde & Gestion d'erreurs
# ═══════════════════════════════════════════

import enum
import os
import json
from datetime import datetime  # pour ajouter la date automatiquement

 #─── Configuration ───
FICHIER_SAUVERGARDE = "budget_data.json"
CATEGORIES = ["Logement", "Alimentation", "Transport", "Loisirs", "Santé", "Autre"]

# ════════════════════════════════
# FONCTIONS UTILITAIRES
# ════════════════════════════════

def demander_nombre(message, minimum=0):
    """Demander un nombre valide à l'utilisateur"""
    while True:
        try:
            valeur=float(input(message))
            if valeur <minimum:
                print(f"⚠️ Ton nombre ne doit pas être inférieur à {minimum}")
                continue
            return valeur
        except ValueError:
            print("❌ Ceci n'est pas un nombre.")


def demander_categorie():
    """ Affiche la catégorie et demande un choix"""
    print("Les différentes catégorie disponible")
    for i, cat in enumerate(CATEGORIES):
        print(f"{i+1} : {cat}")
    
    while True:
        try:
            choix = int(input("Fait ton choix:"))
            if 1<= choix <= len(CATEGORIES):
                return CATEGORIES[choix-1]
            print(f"  ⚠️  Choisis entre 1 et {len(CATEGORIES)}")
        except ValueError:
            print("❌ Ton choix n'est pas valide. Merci de recommencer")


# ════════════════════════════════
# FONCTIONS DE SAUVEGARDE/CHARGEMENT
# ════════════════════════════════

def sauvegarder(donnees, fichier=FICHIER_SAUVERGARDE):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=4)
    print("  💾 Données sauvegardées !")

def charger(fichier=FICHIER_SAUVERGARDE):
    if os.path.exists(fichier):
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                donnees = json.load(f)
            if "depenses" not in donnees or "revenus" not in donnees:
                donnees = {"revenus": donnees.get("revenus", 0), "depenses": donnees.get("depenses", [])}
            print(f"  📂 {len(donnees['depenses'])} dépenses chargées depuis la sauvegarde.")
            return donnees
        except json.JSONDecodeError:
            print("  ⚠️ Fichier de sauvegarde invalide ou vide. On repart de zéro.")
            return {"revenus": 0, "depenses": []}
    else:
        print("  📭 Aucune sauvegarde trouvée.")
        return {"revenus": 0, "depenses": []}

# ════════════════════════════════
# FONCTIONS DU MENU
# ════════════════════════════════

def definir_revenus(donnees):
     """Définir ou modifier les revenus"""
     donnees["revenus"] = demander_nombre("Nouveau revenus mensuel :")
     sauvegarder(donnees)
     print(f"  ✅ Revenus mis à jour : {donnees['revenus']:.2f}€\n")

def ajouter_depense(donnees):
    """ Ajouter une nouvelle dépense"""
    print("\n  ➕ NOUVELLE DÉPENSE")
    print("  " + "-" * 30)

    nom = input("  Nom : ").strip()
    if nom == "":
        print("  ❌ Le nom ne peut pas être vide !")
        return
    categorie = demander_categorie()
    montant = demander_nombre("Montant de la dépense mensuele :")
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    depense = {"nom" : nom, 
    "montant": montant, 
    "categorie" : categorie, 
    "date" : date}

    donnees["depenses"].append(depense)
    sauvegarder(donnees)
    print(f"\n  ✅ '{nom}' ({montant:.2f}€) ajouté en [{categorie}] !\n")

def supprimer_depense(donnees):
    """Supprimer une dépense existante"""
    if len(donnees["depenses"]) == 0:
        print("\n  📭 Aucune dépense à supprimer.\n")
        return
    
    afficher_depenses(donnees)

    while True:
        try :
            num = int(input("Entrer le numéro de la dépense à supprimer(0 = Annuler l'opération) :"))
            if num == 0:
                print("  ↩️  Annulé.")
                return
            if 1<= num <= len(donnees["depenses"]):
                supprimee = donnees["depenses"].pop(num-1)
                sauvegarder(donnees)
                print(f"  🗑️  '{supprimee['nom']}' supprimé !\n")
                return
            print(f"  ⚠️  Choisis entre 1 et {len(donnees['depenses'])}")
        except ValueError:
            print("  ❌ Entre un numéro !")


def afficher_depenses(donnees):
    """Afficher toutes les dépenses"""
    deps = donnees["depenses"]
    if len(deps) == 0:
        print("\n  📭 Aucune dépense enregistrée.\n")
        return

    print(f"\n  {'#':<4} {'Nom':<18} {'Montant':>9} {'Catégorie':<14} {'Date':<12}")
    print("  " + "-" * 61)
    for i, dep in enumerate(deps):
        date_courte = dep.get("date", "?")[:10]
        print(f"  {i+1:<4} {dep['nom']:<18} {dep['montant']:>8.2f}€ {dep['categorie']:<14} {date_courte}")
    
    total = sum(dep["montant"] for dep in deps)
    print("  " + "-" * 61)
    print(f"  {'TOTAL':<22} {total:>8.2f}€\n")


def voir_par_categorie(donnees):
    """Afficher les dépenses groupées par catégorie"""
    deps = donnees["depenses"]
    if len(deps) == 0:
        print("\n  📭 Aucune dépense enregistrée.\n")
        return
    
    categories ={}
    for dep in deps:
        cat = dep["categorie"]
        if cat not in categories:
            categories[cat]=[]
        categories[cat].append(dep)
    print("\n  === 📊 DÉPENSES PAR CATÉGORIE ===\n")
    for cat, liste_deps in sorted(categories.items()):
        total_cat = sum(d["montant"] for d in liste_deps)
        print(f"  📁 {cat} — {total_cat:.2f}€")
        for dep in liste_deps:
            print(f"     └─ {dep['nom']}: {dep['montant']:.2f}€")
        print()


def afficher_rapport(donnees):
    """Afficher le rapport complet"""
    revenus = donnees["revenus"]
    deps = donnees["depenses"]

    if revenus == 0:
        print("\n  ⚠️  Définis d'abord tes revenus (option 1) !\n")
        return

    total = sum(dep["montant"] for dep in deps)
    reste = revenus - total
    pourcentage = (total / revenus * 100) if revenus > 0 else 0

    print("\n  " + "═" * 44)
    print("          📊 RAPPORT MENSUEL")
    print("  " + "═" * 44)
    print(f"  💵 Revenus       : {revenus:>10.2f}€")
    print(f"  💸 Dépenses      : {total:>10.2f}€")
    print(f"  💰 Reste         : {reste:>10.2f}€")
    print(f"  📈 Utilisé       : {pourcentage:>9.1f}%")
    print("  " + "-" * 44)

    # Barre visuelle
    barre_pleine = int(pourcentage / 5)
    barre_vide = 20 - barre_pleine
    couleur = "🟩" if pourcentage < 70 else "🟨" if pourcentage < 90 else "🟥"
    print(f"  [{couleur * min(barre_pleine, 20)}{'⬜' * max(barre_vide, 0)}] {pourcentage:.0f}%")

    print("  " + "-" * 44)
    if reste > 500:
        print("  ✅ Excellent ! Belle marge de manœuvre.")
    elif reste > 100:
        print("  👍 Correct, mais reste vigilant.")
    elif reste > 0:
        print("  ⚠️  Budget très serré !")
    else:
        print("  🚨 ALERTE : Tu dépenses plus que tu ne gagnes !")

    print("  " + "═" * 44 + "\n")


# ════════════════════════════════
# PROGRAMME PRINCIPAL
# ════════════════════════════════

def maint():
    """Fonction principale du programme"""
    print("╔══════════════════════════════════════╗")
    print("║      🏦 BUDGET APP v3               ║")
    print("║   💾 Avec sauvegarde automatique !   ║")
    print("╚══════════════════════════════════════╝\n")

    donnees = charger()

    if donnees["revenus"] == 0:
        print("\n  🆕 Première utilisation !")
        donnees["revenus"] = demander_nombre("  Tes revenus mensuels (€) : ", minimum=1)
        sauvegarder(donnees)
    
    while True:
        print("  ┌──── MENU ────────────────────┐")
        print("  │ 1. 💵 Modifier les revenus    │")
        print("  │ 2. ➕ Ajouter une dépense     │")
        print("  │ 3. 🗑️  Supprimer une dépense  │")
        print("  │ 4. 📋 Voir les dépenses       │")
        print("  │ 5. 📊 Voir par catégorie      │")
        print("  │ 6. 📈 Rapport complet         │")
        print("  │ 7. 🚪 Quitter                 │")
        print("  └─────────────────────────────┘")

        choix = input("\n  Ton choix (1-7) : ").strip()

        if choix == "1":
            definir_revenus(donnees)
        elif choix == "2":
            ajouter_depense(donnees)
        elif choix == "3":
            supprimer_depense(donnees)
        elif choix == "4":
            afficher_depenses(donnees)
        elif choix == "5":
            voir_par_categorie(donnees)
        elif choix == "6":
            afficher_rapport(donnees)
        elif choix == "7":
            sauvegarder(donnees)
            print("\n  👋 À bientôt ! Tes données sont sauvegardées.\n")
            break
        else:
            print("  ❌ Choix invalide (1-7)\n")

# Lancer le programme
maint()





