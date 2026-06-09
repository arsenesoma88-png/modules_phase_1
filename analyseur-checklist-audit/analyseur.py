import pandas as pd

def charger_fichier(path):
    """Charge le fichier Excel et normalise les colonnes"""
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip().str.lower()
    df["statut"] = df["statut"].astype(str).str.strip().str.lower()
    return df

def compter_statuts(df):
    """Compte les statuts attendus"""
    return {
        "Satisfaisant": int((df["statut"] == "satisfaisant").sum()),
        "Non_satisfaisant": int((df["statut"] == "non satisfaisant").sum()),
        "Sans_objet": int((df["statut"] == "sans objet").sum()),
        "Non_evalue": int((df["statut"] == "non évalué").sum())
    }

def calculer_taux(statistique, statuts_inattendus):
    """Calcule le taux de conformité"""
    if statuts_inattendus:
        print("Statuts inattendus détectés :", statuts_inattendus)
        print("Taux non calculé : corrigez les données avant de relancer.")
        return None

    denominateur = statistique["Satisfaisant"] + statistique["Non_satisfaisant"] + statistique["Non_evalue"]
    if denominateur == 0:
        print("Toutes les questions sont sans objet, le taux est non calculable")
        return None

    return statistique["Satisfaisant"] / denominateur

def extraire_non_satisfaisants(df, output_path="data/actions_correctives.csv"):
    """Extrait les questions non satisfaisantes et les écrit en CSV"""
    df_non_satisfaisant = df[df["statut"] == "non satisfaisant"]
    if {"numero", "question", "commentaire"}.issubset(df_non_satisfaisant.columns):
        df_non_satisfaisant[["numero", "question", "commentaire"]].to_csv(output_path, index=False)
    else:
        print("Colonnes attendues absentes, export complet.")
        df_non_satisfaisant.to_csv(output_path, index=False)

def main():
    # Charger et normaliser
    df = charger_fichier("data/checklist_test.xlsx")

    # Statuts attendus
    statuts_attendus = {"satisfaisant", "non satisfaisant", "sans objet", "non évalué"}
    statuts_inattendus = set(df["statut"]) - statuts_attendus

    # Comptages
    statistique = compter_statuts(df)
    print("Récapitulatif des statuts :", statistique)

    # Taux de conformité
    taux_conformite = calculer_taux(statistique, statuts_inattendus)
    if taux_conformite is not None:
        print(f"Taux de conformité : {taux_conformite:.2%}")

    # Export des non satisfaisants
    extraire_non_satisfaisants(df)

if __name__ == "__main__":
    main()