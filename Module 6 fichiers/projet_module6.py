def impot(revenu_imposable):
    """La fonction impot reçoit un revenu imposable et renvoit l'impôt progressif"""
    
    if revenu_imposable <= 30000:
        impot = 0
    elif revenu_imposable <= 50000:
        impot = (revenu_imposable - 30000) * 0.10
    elif revenu_imposable <= 80000:
        impot = 20000 * 0.10 + (revenu_imposable - 50000) * 0.15
    else:
        impot = 20000 * 0.10 + 30000 * 0.15 + (revenu_imposable - 80000) * 0.20

    return impot

while True:
    try:
        N = int(input("Saisis le nombre d'employés : "))
        if N >= 1:
            break
    except ValueError:
        print("Ce n'est pas un nombre entier supérieur à 0, recommence.")
    
total_bruts = 0
total_impots = 0
total_nets = 0
employes = {}
mieux_paye = ""
salaire_max = 0

for k in range(1, N+1):
    print(f"===== Employé n°{k} =====")
    nom = input("Saisis le nom : ")
    while True:
        try:        
            brut = int(input("Saisis le salaire brut mensuel en FCFA : "))
            if brut > 0:
                break
        except ValueError:
            print("Ce n'est pas un nombre entier supérieur à 0, recommence.")
    employes[nom] = brut

with open("bulletin.txt", "w") as f:
    for nom, salaire in employes.items():
        total_bruts = total_bruts + salaire
        retenue_sociale = salaire / 10     # la retenue sociale représente 10% du salaire brut mensuel
        revenu_imposable = salaire - retenue_sociale
        impot_calcule = impot(revenu_imposable)
        total_impots = total_impots + impot_calcule
        net = revenu_imposable - impot_calcule
        if net > salaire_max:
            salaire_max = net
            mieux_paye = nom
        
        f.write(f"{nom} : net {net:.2f}\n") 
        total_nets = total_nets + net
    f.write(f"Total net : {total_nets:.2f}\n")
    f.write(f"Mieux payé : {mieux_paye}\n")
    
print("Bulletin complété")