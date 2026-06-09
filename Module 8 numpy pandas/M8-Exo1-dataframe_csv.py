import pandas as pd

df = pd.DataFrame({"ville":["Berlin","Londres","Ottawa"],"population":[2780000,5846255,15048556]})
df.to_csv("sortie.csv", index=False)
df_sortie = pd.read_csv("sortie.csv")
population_totale = df_sortie["population"].sum()
print("Population totale : ",population_totale)