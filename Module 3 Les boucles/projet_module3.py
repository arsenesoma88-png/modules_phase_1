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
    revenue_imposable = brut-retenue_sociale
    if revenue_imposable <= 30000:
        impot = 0
    elif revenue_imposable <= 50000:
        impot = (revenue_imposable - 30000) * 0.10
    elif revenue_imposable <= 80000:
        impot = 20000 * 0.10 + (revenue_imposable - 50000) * 0.15
    else:
        impot = 20000 * 0.10 + 30000 * 0.15 + (revenue_imposable - 80000) * 0.20

    total_impots = total_impots + impot
    net = revenue_imposable - impot
    total_nets = total_nets + net
net_moyen = total_nets / N
print("===== ETAT DES SALAIRE  =====")
print(f"Total brut mensuel : {total_bruts:.2f} FCFA")
print(f"Total impots        : {total_impots:.2f} FCFA")
print(f"Total net mensuel  : {total_nets:.2f} FCFA")
print(f"Net moyen   : {net_moyen:.2f} FCFA")
print("==============================")


