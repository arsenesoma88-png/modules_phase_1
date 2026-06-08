salaire_brut_mensuel = int(input("Saisis le salaire brut mensuel en FCFA : "))
retenue_sociale = salaire_brut_mensuel/10     # la retenue sociale représente 10% du salaire brut mensuel
retenue_imposable = salaire_brut_mensuel-retenue_sociale
if retenue_imposable <= 30000:
    impot = 0
elif retenue_imposable <= 50000:
    impot = (retenue_imposable - 30000) * 0.10
elif retenue_imposable <= 80000:
    impot = 20000 * 0.10 + (retenue_imposable - 50000) * 0.15
else:
    impot = 20000 * 0.10 + 30000 * 0.15 + (retenue_imposable - 80000) * 0.20

salaire_net_mensuel=retenue_imposable - impot
salaire_net_annuel = salaire_net_mensuel*12
print("===== BULLETIN SIMPLIFIÉ =====")
print(f"Salaire brut mensuel : {salaire_brut_mensuel:.2f} FCFA")
print(f"Retenue sociale        : {retenue_sociale:.2f} FCFA")
print(f"Retenue imposable        : {retenue_imposable:.2f} FCFA")
print(f"Impôt        : {impot:.2f} FCFA")
print(f"Salaire net mensuel  : {salaire_net_mensuel:.2f} FCFA")
print(f"Salaire net annuel   : {salaire_net_annuel:.2f} FCFA")
print("==============================")


