import pandas as pd

denree = pd.DataFrame({"produit":["riz", "huile", "sucre"],"prix":[15000, 9000, 6000]})
denree["prix_promo"] = denree["prix"] * 80/100
print(denree)

