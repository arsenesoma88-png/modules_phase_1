def impot(revenu_imposable):
    """impot recoit un revenu imposable et renvoi l'impôt progressif"""
    
    if revenu_imposable <= 30000:
        impot = 0
    elif revenu_imposable <= 50000:
        impot = (revenu_imposable - 30000) * 0.10
    elif revenu_imposable <= 80000:
        impot = 20000 * 0.10 + (revenu_imposable - 50000) * 0.15
    else:
        impot = 20000 * 0.10 + 30000 * 0.15 + (revenu_imposable - 80000) * 0.20

    return impot

def salaire_net(brut): 
    retenue_sociale = brut/10     # la retenue sociale représente 10% du salaire brut mensuel
    revenu_impot = brut-retenue_sociale
    impot_salaire = impot(revenu_impot)
    net = revenu_impot - impot_salaire
    return net

while True:
    N = int(input("Saisis le nombre d'employés : "))
    if N >= 1:
        break
total_bruts = 0
total_impots = 0
total_nets = 0

for k in range(1, N+1):
    print(f"===== Employé n°{k} =====")
    brut = int(input("Saisis le salaire brut mensuel en FCFA : "))
    total_bruts = total_bruts + brut
    retenue_sociale = brut/10     # la retenue sociale représente 10% du salaire brut mensuel
    revenu_imposable = brut-retenue_sociale
    impot_calcule = impot(revenu_imposable)
    total_impots = total_impots + impot_calcule
    net = salaire_net(brut)
    total_nets = total_nets + net
net_moyen = total_nets / N
print("===== ETAT DES SALAIRE  =====")
print(f"Total brut mensuel : {total_bruts:.2f} FCFA")
print(f"Total impots        : {total_impots:.2f} FCFA")
print(f"Total net mensuel  : {total_nets:.2f} FCFA")
print(f"Net moyen   : {net_moyen:.2f} FCFA")
print("==============================")


