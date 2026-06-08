anciennete = 8          # années
note = 12               # /20
est_cadre = False        # booléen

eligible = (anciennete >= 5) and ((note >= 14) or est_cadre)
print(f"Éligible : {eligible}")