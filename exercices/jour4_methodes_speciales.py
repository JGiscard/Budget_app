class Depense:

    def __init__(self, nom, montant, categorie):
        self.nom = nom
        self.montant = montant
        self.categorie = categorie
    
    # ─── __str__ : comment l'objet s'AFFICHE ───
    # Appelée automatiquement par print()
    def __str__(self):
        return f"{self.nom} : {self.montant:.2f}€ [{self.categorie}]"
    
    # ─── __repr__ : représentation technique ───
    # Appelée dans le terminal interactif ou dans les listes
    def __repr__(self):
        return f"Depense('{self.nom}', {self.montant}, '{self.categorie}')"
    
    # ─── __eq__ : comparer deux dépenses ───
    # Permet d'utiliser == entre deux objets
    def __eq__(self, autre):
        return self.nom == autre.nom and self.montant == autre.montant
    
     # ─── __lt__ : comparer "moins que" ───
    # Permet de trier les dépenses par montant
    def __lt__(self, autre):
        return self.montant < autre.montant

    
#Tests
loyer = Depense("Loyer", 800, "Logement")
courses = Depense("Courses", 65.50, "Alimentation")
netflix = Depense("Netflix", 15.99, "Loisirs")
loyer2 = Depense("Loyer", 800, "Logement")

# __str__ en action
print(loyer)      # → Loyer : 800.00€ [Logement]
# Sans __str__, ça afficherait : <__main__.Depense object at 0x...>  😱

# __repr__ en action
print(repr(loyer))  # → Depense('Loyer', 800, 'Logement')

# __eq__ en action
print(f"\nloyer == loyer2 ? {loyer == loyer2}")      # → True
print(f"loyer == courses ? {loyer == courses}")       # → False

# __lt__ en action : permet de TRIER !
depenses = [loyer, courses, netflix]
depenses_triees = sorted(depenses)

print("\n📊 Dépenses triées par montant :")
for dep in depenses_triees:
    print(f"  {dep}")