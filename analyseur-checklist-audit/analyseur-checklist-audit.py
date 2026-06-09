import pandas as pd

# Charger le fichier Excel
df = pd.read_excel("data/checklist_test.xlsx")

# Normaliser la colonne 'statut' : enlever espaces et mettre en minuscule
df["statut"] = df["statut"].astype(str).str.strip().str.lower()

# Statuts attendus
statuts_attendus = {
    "satisfaisant": "Satisfaisant",
    "non satisfaisant": "Non satisfaisant",
    "sans objet": "Sans objet",
    "non évalué": "Non évalué"
}

# Comptage par statut
statistique = {}
statistique["satisfaisant"] = (df["statut"] == "satisfaisant").sum()
statistique["non_satisfaisant"] = (df["statut"] == "non satisfaisant").sum()
statistique["sans_objet"] = (df["statut"] == "sans objet").sum()
statistique["non_evalue"] = (df["statut"] == "non évalué").sum()

# Vérifier cohérence : somme des comptages = nombre total de lignes
total_comptage = sum(statistique.values())
if total_comptage != len(df):
    statuts_inattendus = set(df["statut"]) - set(statuts_attendus.keys())
    print("Statuts inattendus détectés :", statuts_inattendus)

# Calcul du taux de conformité
denominateur = statistique["satisfaisant"] + statistique["non_satisfaisant"] + statistique["non_evalue"]

if denominateur == 0:
    print("Toutes les questions sont sans objet → taux non calculable")
    taux_conformite = None
else:
    taux_conformite = statistique["satisfaisant"] / denominateur

# Export des questions non satisfaisantes
df_non_satisfaisant = df[df["statut"] == "non satisfaisant"]
df_non_satisfaisant[["numero", "question", "commentaire"]].to_csv("data/actions_correctives.csv", index=False)

# Résultats
print("Récapitulatif des statuts :", statistique)
if taux_conformite is not None:
    print(f"Taux de conformité : {taux_conformite:.2%}")
