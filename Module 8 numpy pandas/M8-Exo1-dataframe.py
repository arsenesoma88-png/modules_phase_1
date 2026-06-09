import pandas as pd

denree = pd.DataFrame({"produit":["riz", "huile", "sucre"],"prix":[15000, 9000, 6000]})

print(denree)
print("Somme des prix : ", denree["prix"].sum())
