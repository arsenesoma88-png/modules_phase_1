salaire_brut_mensuel = int(input("Saisis le salaire brut mensuel en FCFA : "))
retenue_sociale = salaire_brut_mensuel/10     # la retenue sociale représente 10% du salaire brut mensuel
revenu_imposable = salaire_brut_mensuel-retenue_sociale
if revenu_imposable <= 30000:
    impot = 0
elif revenu_imposable <= 50000:
    impot = (revenu_imposable - 30000) * 0.10
elif revenu_imposable <= 80000:
    impot = 20000 * 0.10 + (revenu_imposable - 50000) * 0.15
else:
    impot = 20000 * 0.10 + 30000 * 0.15 + (revenu_imposable - 80000) * 0.20

salaire_net_mensuel=revenu_imposable - impot
salaire_net_annuel = salaire_net_mensuel*12
print("===== BULLETIN SIMPLIFIÉ =====")
print(f"Salaire brut mensuel : {salaire_brut_mensuel:.2f} FCFA")
print(f"Retenue sociale        : {retenue_sociale:.2f} FCFA")
print(f"Retenue imposable        : {revenu_imposable:.2f} FCFA")
print(f"Impôt        : {impot:.2f} FCFA")
print(f"Salaire net mensuel  : {salaire_net_mensuel:.2f} FCFA")
print(f"Salaire net annuel   : {salaire_net_annuel:.2f} FCFA")
print("==============================")


