#═══════════════════════════════════════════
# BUDGET MANAGER — Organiser tout dans une classe
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
    

    #Affichage
    def __str__(self):
        return (f"BudgetManager: {self.revenus:.2f}€ revenus, "
                f"{len(self.depenses)} dépenses, "
                f"{self.reste():.2f}€ restant")

    def __len__(self):
        return len(self.depenses)

# Test de la classe
if __name__ == "__main__":
    print("=== Test BudgetManager ===\n")

    bm = BudgetManager("test_budget.json")
    bm.revenus = 2000
    bm.sauvegarder()

    # Ajouter des dépenses
    bm.ajouter("Loyer", 800, "Logement")
    bm.ajouter("Courses", 250, "Alimentation")
    bm.ajouter("Métro", 75, "Transport")
    bm.ajouter("Restaurant", 45, "Alimentation")
    bm.ajouter("Netflix", 15.99, "Loisirs")
    bm.ajouter("Médecin", 25, "Santé")

    # Afficher l'état
    print(f"\n{bm}")
    print(f"Nombre de dépenses : {len(bm)}")

    # Lister les dépenses
    print("\n📋 Toutes les dépenses :")
    for i, dep in enumerate(bm.depenses):
        print(f"  {i+1}. {dep}")

    # Calculs
    print(f"\n💰 Total dépenses : {bm.total_depenses():.2f}€")
    print(f"💵 Reste : {bm.reste():.2f}€")
    print(f"📊 Utilisé : {bm.pourcentage_utilise():.1f}%")

    # Par catégorie
    print("\n📁 Par catégorie :")
    for cat, deps in bm.par_categorie().items():
        total_cat = sum(d.montant for d in deps)
        print(f"  {cat} : {total_cat:.2f}€ ({len(deps)} dépenses)")

    # Top 3
    print("\n🏆 Top 3 dépenses :")
    for dep in bm.top_depenses(3):
        print(f"  {dep}")


