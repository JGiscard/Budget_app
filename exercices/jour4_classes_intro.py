# ═══════════════════════════════════════════
# LES CLASSES — Comprendre le concept
# ═══════════════════════════════════════════

# 🏗️ ANALOGIE : Une classe c'est un MOULE à gâteaux
# Le moule (classe) définit la FORME
# Chaque gâteau (objet) est UNIQUE mais a la même forme

# Jusqu'ici tu as utilisé des classes sans le savoir :
# - "Bonjour" est un OBJET de la CLASSE str
# - [1, 2, 3] est un OBJET de la CLASSE list
# - {"nom": "Ali"} est un OBJET de la CLASSE dict

# ═══════════════════════════════════════════
# PREMIÈRE CLASSE — Dépense
# ═══════════════════════════════════════════

class Depense:
    """Représente une dépense avec ses détails."""
    def __init__(self, nom, montant, categorie):
        self.nom = nom
        self.montant = montant
        self.categorie = categorie
    
    def afficher(self):
        """Affciche les dépenses de manière formatée."""
        print(f"  {self.nom} : {self.montant:.2f}€ [{self.categorie}]")
    
    def est_grosse_depense(self, seuil = 100):
        """ vérifie si une dépense dépasse un seuil spécifique."""
        return self.montant > seuil


# ─── Créer des OBJETS (= instances de la classe) ───

loyer = Depense("Loyer", 500, "Logement")
courses = Depense("Courses", 100, "Alimentation")
netflix = Depense("Netflix", 15, "Loisirs")

# loyer, courses, netflix sont 3 OBJETS différents
# mais ils ont tous la même STRUCTURE (nom, montant, categorie)

print("=== Nos dépenses ===")
loyer.afficher()
courses.afficher()
netflix.afficher()

# Accéder aux attributs directement
print(f"Loyer : {loyer.nom} - {loyer.montant}€ - {loyer.categorie}")
# Utiliser une méthode
print(f"\nLoyer est une grosse dépense ? {loyer.est_grosse_depense()}")
print(f"Netflix est une grosse dépense ? {netflix.est_grosse_depense()}")
print(f"Courses > 50€ ? {courses.est_grosse_depense(50)}")


# On peut mettre les objets dans une LISTE
depenses = [loyer, courses, netflix]
total = sum(dep.montant for dep in depenses)
print(f"\nTotal des dépenses : {total:.2f}€")


# ═══════════════════════════════════════════
# SELF — Le concept le plus déroutant au début
# ═══════════════════════════════════════════

# "self" = "moi, l'objet qui appelle cette méthode"
class CompteBancaire:
    """ Un compte bancaire simple"""
    def __init__(self, proprietaire, solde = 0):
        # Quand on écrit : compte = CompteBancaire("Ali", 1000)
        # Python fait en coulisses : __init__(compte, "Ali", 1000)
        # Donc self = compte (l'objet qu'on est en train de créer)
        self.proprietaire = proprietaire
        self.solde = solde
        self.historique = []
        print (f"compte créé pour {self.proprietaire} avec un solde de {self.solde}€")
    
    def deposer(self, montant):
        """dépose un montant sur le compte"""
        self.solde +=montant
        self.historique.append(f"+{montant}€")
        print(f" 💰 +{montant}€ → Nouveau solde : {self.solde}€")
    
    def retirer(self, montant):
        """retire un montant du compte"""
        if montant > self.solde:
            print(f"❌ Solde insuffisant! {self.solde}€ disponible")
            return
        self.solde -=montant
        self.historique.append(f"-{montant}€")
        print(f" 💰 -{montant}€ → Nouveau solde : {self.solde}€")
    
    def afficher_historique(self):
        """affiche l'historique des opérations"""
        print(f"\nHistorique de {self.proprietaire} :") 
        if len(self.historique) == 0:
            print("Aucune opération enregistrée")
            return
        for operation in self.historique:
            print (f"  {operation}")
        print(f"💰 Solde final : {self.solde}€")

# ─── Créons DEUX comptes SÉPARÉS ───
print("=== Création des comptes ===")
compte_ali = CompteBancaire("Ali", 1000)
compte_marie = CompteBancaire("Marie", 500)

print("\n=== Opérations sur le compte d'Ali ===")
compte_ali.deposer(200)      # self = compte_ali
compte_ali.retirer(50)       # self = compte_ali

print("\n=== Opérations sur le compte de Marie ===")
compte_marie.deposer(1000)   # self = compte_marie
compte_marie.retirer(300)    # self = compte_marie
compte_marie.retirer(2000)   # → solde insuffisant !

# Les historiques sont INDÉPENDANTS
compte_ali.afficher_historique()
compte_marie.afficher_historique()

# ─── La preuve que les objets sont indépendants ───
print(f"Solde Ali   : {compte_ali.solde}€")
print(f"Solde Marie : {compte_marie.solde}€")
print("→ Chaque objet vit sa propre vie !")

        