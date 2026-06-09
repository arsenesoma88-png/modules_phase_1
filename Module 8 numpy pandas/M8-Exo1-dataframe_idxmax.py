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

df = pd.DataFrame({"nom": ["Awa", "Salif", "Fatou", "Ali", "Jacques"], "brut": [100000, 40000, 250000, 74000, 130000]})
df["imposable"] = df["brut"] * 90 / 100
df["impot"] = df["imposable"].apply(impot)
df["net"] = df["imposable"] - df["impot"]
print(df)
print("Le net total : ", df["net"].sum())
print("Le net moyen : ", df["net"].mean())
print(df.loc[df["net"].idxmax(), "nom"])
