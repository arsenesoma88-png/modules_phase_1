salaire_brut_mensuel = int(input("Saisis le salaire brut mensuel en FCFA : "))
retenue_sociale = salaire_brut_mensuel/10     # la retenue sociale représente 10% du salaire brut mensuel
salaire_net_mensuel = salaire_brut_mensuel-retenue_sociale
salaire_net_annuel = salaire_net_mensuel*12
print("===== BULLETIN SIMPLIFIÉ =====")
print(f"Salaire brut mensuel : {salaire_brut_mensuel:.2f} FCFA")
print(f"Retenue (10%)        : {retenue_sociale:.2f} FCFA")
print(f"Salaire net mensuel  : {salaire_net_mensuel:.2f} FCFA")
print(f"Salaire net annuel   : {salaire_net_annuel:.2f} FCFA")
print("==============================")


