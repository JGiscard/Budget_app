# ═══════════════════════════════════════════
# MODULE OS — Interagir avec le système de fichiers
# ═══════════════════════════════════════════

import os
import json

# ─── Vérifier si un fichier existe ───
if os.path.exists("budget_data.json"):
    print("✅ Le fichier budget_data.json existe !")
else:
    print("❌ Le fichier n'existe pas encore.")

def charger_donnees(fichier="budget_data.json"):
    """Charge les données si le fichier existe, sinon retourne un modèle vide"""
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            print(f"📂 Données chargées depuis {fichier}")
            return json.load(f)
    else:
        print("📭 Aucune sauvegarde trouvée, on part de zéro.")
        return {
            "revenus": 0,
            "depenses": []
        }

# Test
donnees = charger_donnees()
print(f"  Revenus : {donnees['revenus']}€")
print(f"  Dépenses : {len(donnees['depenses'])}")

# ─── Autres fonctions utiles de os ───
print(f"\n📁 Dossier actuel : {os.getcwd()}")
print(f"📋 Fichiers ici : {os.listdir('.')}")