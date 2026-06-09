import pandas as pd

def impot(imposable):
    if imposable <= 30000:
        return 0
    elif imposable <= 50000:
        return (imposable - 30000) * 0.10
    elif imposable <= 80000:
        return 20000 * 0.10 + (imposable - 50000) * 0.15
    else:
        return 20000 * 0.10 + 30000 * 0.15 + (imposable - 80000) * 0.20

df = pd.DataFrame({"nom": ["Awa", "Salif", "Fatou"], "brut": [100000, 40000, 250000]})
df.to_csv("employes.csv", index=False)
df = pd.read_csv("employes.csv")
df["retenue"]=df["brut"] * 10 / 100
df["imposable"] = df["brut"] - df["retenue"]
df["impot"] = df["imposable"].apply(impot)
df["net"] = df["imposable"] - df["impot"]
print(df)
print("Le net total : ", df["net"].sum())
print("Le net moyen : ", df["net"].mean())
print("Mieux payé :", df.loc[df["net"].idxmax(), "nom"])

df.to_csv("paie_analysee.csv", index=False)


