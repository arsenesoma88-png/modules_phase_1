import pandas as pd

denree = pd.DataFrame({"produit":["riz", "huile", "sucre"],"prix":[15000, 9000, 6000]})

print("Produits dont le prix est supérieur à 7000 : ", denree[denree["prix"] > 7000])