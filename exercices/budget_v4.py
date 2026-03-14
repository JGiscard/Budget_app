# ═══════════════════════════════════════════
# 🏦 BUDGET APP v4 — Version Orientée Objet
# ═══════════════════════════════════════════

import json
import os
from datetime import datetime

class Depense:
    """ représente une seule dépense"""
    CATEGORIES = ["Logement", "Alimentation", "Transport", "Santé", "Loisirs", "Autres"]

    def __init__(self, nom, montant, categorie, date=None):
        self.nom = nom
        self.montant = montant
        self.categorie = categorie
        self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def __str__(self):
        return f"{self.date} : {self.nom} - {self.montant:.2f}€ [{self.categorie}]"

    def __repr__(self):
        return f"Depense('{self.nom}', {self.montant}, '{self.categorie}', '{self.date}')"
    
    def __lt__(self, autre):
        return self.montant < autre.montant
    
    def to_dict(self):
        return {
            "nom": self.nom,
            "montant": self.montant,
            "categorie": self.categorie,
            "date": self.date
        }
    
    @classmethod
    def from_dict(cls, donnees):
        return cls(
            donnees["nom"], 
            donnees["montant"], 
            donnees["categorie"], 
            donnees.get("date"))


class BudgetManager:
    """Gère l'ensemble du budget : revenus, dépenses, sauvegarde"""

    def __init__(self, fichier="budget_data.json"):
        self.fichier = fichier
        self.revenus = 0
        self.depenses = []          # liste d'objets Depense
        self.charger()              # charge automatiquement au démarrage

    # ── Sauvegarde / Chargement ──    
    
    def sauvegarder(self):
        """ Sauvergarde l'état complet dans un fichier JSON"""
        donnees = {
            "revenus": self.revenus,
            "depenses": [dep.to_dict() for dep in self.depenses]
        }
        with open(self.fichier, "w", encoding = "utf-8") as f:
            json.dump(donnees, f, ensure_ascii = False,indent = 4)
    
    def charger(self):
        """ Charge les données depuis un fichier JSON"""
        if os.path.exists(self.fichier,):
            with open(self.fichier, "r", encoding = "utf-8") as f:
                donnees = json.load(f)
            self.revenus = donnees.get("revenus", 0)
            self.depenses = [
                Depense.from_dict(d) for d in donnees.get("depenses",[])
            ]
            print(f"  📂 {len(self.depenses)} dépenses chargées.")
        else:
            print("  📭 Aucune sauvegarde trouvée.")

    #Actions principales

    def ajouter(self, nom, montant, categorie):
        """Ajoute une nouvelle dépense"""
        dep = Depense(nom,montant,categorie)
        self.depenses.append(dep)
        self.sauvegarder()
        return dep
    
    def supprimer(self, index):
        """ Supprime une dépense par son index"""
        if 0 <= index <= len(self.depenses):
            supprimee = self.depenses.pop(index)
            self.sauvegarder()
            return supprimee
        return None
    
    #Calcul

    def total_depenses(self):
        """ Calcul le total des dépenses"""
        return(sum(dep.montant for dep in self.depenses))
    
    def reste (self):
        """ Calcul le solde restant après toute les dépenses"""
        return self.revenus - self.total_depenses()
    
    def pourcentage_utilise(self):
        """ Calcul le pourcentage des revenus qui a été utilisé """
        if self.revenus == 0:
            return 0
        return (self.total_depenses()/self.revenus) * 100
    
    def par_categorie(self):
        """ Regroupe les dépenses par catégorie"""
        categories = {}
        for dep in self.depenses:
            if dep.categorie not in categories:
                categories[dep.categorie] = []
            categories[dep.categorie].append(dep)
        return categories
    
    def top_depenses(self, n=3):
        """ Retourne les N plus grosses dépenses"""
        return sorted(self.depenses, reverse=True)[:n]
    def rechercher(self, terme):
        """Recherche des dépenses par nom"""
        terme = terme.lower()
        return [dep for dep in self.depenses if terme in dep.nom.lower()]
    

    #Affichage
    def __str__(self):
        return (f"BudgetManager: {self.revenus:.2f}€ revenus, "
                f"{len(self.depenses)} dépenses, "
                f"{self.reste():.2f}€ restant")

    def __len__(self):
        return len(self.depenses)


# ════════════════════════════════
# CLASSE APPLICATION (Interface utilisateur)
# ════════════════════════════════

class BudgetApp:
    """Interface utilisateur — gère l'affichage et les menus"""
    def __init__(self):
        self.manager = BudgetManager()
    
    # ── Utilitaires de saisie ──

    def demander_nombre(self, message, minimum=0):
        while True:
            try:
                valeur = float(input(message))
                if valeur < minimum:
                    print(f"  ⚠️  Minimum : {minimum}")
                    continue
                return valeur
            except ValueError:
                print("  ❌ Nombre invalide !")
    
    def demander_categorie(self):
        print("  Catégories :")
        for i, cat in enumerate(Depense.CATEGORIES):
            print(f"    {i+1}. {cat}")
        while True:
            try:
                choix = int(input("  Numéro : "))
                if 1 <= choix <= len(Depense.CATEGORIES):
                    return Depense.CATEGORIES[choix - 1]
                print(f"  ⚠️  Entre 1 et {len(Depense.CATEGORIES)}")
            except ValueError:
                print("  ❌ Nombre invalide !")
    
     # ── Actions du menu ──

    def modifier_revenus(self):
        print(f"\n  💵 Revenus actuels : {self.manager.revenus:.2f}€")
        self.manager.revenus = self.demander_nombre("  Nouveaux revenus : ", minimum=1)
        self.manager.sauvegarder()
        print(f"  ✅ Revenus : {self.manager.revenus:.2f}€\n")
    
    def ajouter_depense(self):
        print("\n  ➕ NOUVELLE DÉPENSE")
        nom = input("  Nom : ").strip()
        if not nom:
            print("  ❌ Nom vide !")
            return
        montant = self.demander_nombre("  Montant (€) : ", minimum=0.01)
        categorie = self.demander_categorie()
        dep = self.manager.ajouter(nom, montant, categorie)
        print(f"  ✅ Ajouté : {dep}\n")
    
    def supprimer_depense(self):
        if not self.manager.depenses:
            print("\n  📭 Aucune dépense.\n")
            return
        self.afficher_depenses()
        while True:
            try:
                num = int(input("  Numéro à supprimer (0 = annuler) : "))
                if num == 0:
                    return
                dep = self.manager.supprimer(num - 1)
                if dep:
                    print(f"  🗑️  Supprimé : {dep}\n")
                    return
                print(f"  ⚠️  Numéro invalide")
            except ValueError:
                print("  ❌ Nombre invalide !")
    
    def afficher_depenses(self):
        deps = self.manager.depenses
        if not deps:
            print("\n  📭 Aucune dépense.\n")
            return
        print(f"\n  {'#':<4} {'Nom':<18} {'Montant':>9} {'Catégorie':<14} {'Date':<12}")
        print("  " + "─" * 61)
        for i, dep in enumerate(deps):
            print(f"  {i+1:<4} {dep.nom:<18} {dep.montant:>8.2f}€ {dep.categorie:<14} {dep.date[:10]}")
        print("  " + "─" * 61)
        print(f"  {'TOTAL':<22} {self.manager.total_depenses():>8.2f}€\n")
    
    def voir_categories(self):
        cats = self.manager.par_categorie()
        if not cats:
            print("\n  📭 Aucune dépense.\n")
            return
        print("\n  === 📊 PAR CATÉGORIE ===\n")
        for cat, deps in sorted(cats.items()):
            total = sum(d.montant for d in deps)
            pct = (total / self.manager.total_depenses() * 100) if self.manager.total_depenses() > 0 else 0
            print(f"  📁 {cat} — {total:.2f}€ ({pct:.0f}%)")
            for dep in deps:
                print(f"     └─ {dep.nom}: {dep.montant:.2f}€")
            print()

    def rechercher(self):
        terme = input("\n  🔍 Rechercher : ").strip()
        if not terme:
            return
        resultats = self.manager.rechercher(terme)
        if resultats:
            print(f"  {len(resultats)} résultat(s) :")
            for dep in resultats:
                print(f"    {dep}")
        else:
            print("  Aucun résultat.")
        print()

    def rapport(self):
        if self.manager.revenus == 0:
            print("\n  ⚠️  Définis tes revenus d'abord !\n")
            return

        pct = self.manager.pourcentage_utilise()

        print("\n  " + "═" * 44)
        print("          📊 RAPPORT MENSUEL")
        print("  " + "═" * 44)
        print(f"  💵 Revenus       : {self.manager.revenus:>10.2f}€")
        print(f"  💸 Dépenses      : {self.manager.total_depenses():>10.2f}€")
        print(f"  💰 Reste         : {self.manager.reste():>10.2f}€")
        print(f"  📈 Utilisé       : {pct:>9.1f}%")
        print("  " + "─" * 44)

        barre_pleine = int(min(pct, 100) / 5)
        barre_vide = 20 - barre_pleine
        icone = "🟩" if pct < 70 else "🟨" if pct < 90 else "🟥"
        print(f"  [{icone * barre_pleine}{'⬜' * barre_vide}] {pct:.0f}%")

        print("  " + "─" * 44)

        # Top 3
        top = self.manager.top_depenses(3)
        if top:
            print("\n  🏆 Top 3 dépenses :")
            for i, dep in enumerate(top):
                print(f"    {i+1}. {dep}")

        print("  " + "═" * 44 + "\n")

    # ── Boucle principale ──

    def lancer(self):
        print("╔══════════════════════════════════════╗")
        print("║      🏦 BUDGET APP v4               ║")
        print("║   🎯 Version Orientée Objet          ║")
        print("╚══════════════════════════════════════╝\n")

        if self.manager.revenus == 0:
            print("  🆕 Première utilisation !")
            self.manager.revenus = self.demander_nombre("  Revenus mensuels (€) : ", minimum=1)
            self.manager.sauvegarder()
        else:
            print(f"  👋 Content de te revoir ! ({len(self.manager.depenses)} dépenses)")

        while True:
            print("  ┌──── MENU ─────────────────────┐")
            print("  │ 1. 💵 Modifier revenus         │")
            print("  │ 2. ➕ Ajouter une dépense      │")
            print("  │ 3. 🗑️  Supprimer une dépense   │")
            print("  │ 4. 📋 Voir les dépenses        │")
            print("  │ 5. 📊 Par catégorie            │")
            print("  │ 6. 🔍 Rechercher               │")
            print("  │ 7. 📈 Rapport complet          │")
            print("  │ 8. 🚪 Quitter                  │")
            print("  └────────────────────────────────┘")

            choix = input("\n  Ton choix (1-8) : ").strip()

            actions = {
                "1": self.modifier_revenus,
                "2": self.ajouter_depense,
                "3": self.supprimer_depense,
                "4": self.afficher_depenses,
                "5": self.voir_categories,
                "6": self.rechercher,
                "7": self.rapport,
            }

            if choix == "8":
                self.manager.sauvegarder()
                print("\n  👋 À bientôt ! Données sauvegardées. 💾\n")
                break
            elif choix in actions:
                actions[choix]()
            else:
                print("  ❌ Choix invalide (1-8)\n")



# ════════════════════════════════
# LANCEMENT
# ════════════════════════════════

if __name__ == "__main__":
    app = BudgetApp()
    app.lancer()
