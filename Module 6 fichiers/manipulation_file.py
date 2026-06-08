def impot(revenu_imposable):
    if revenu_imposable <= 30000:
        return 0
    elif revenu_imposable <= 50000:
        return (revenu_imposable - 30000) * 0.10
    elif revenu_imposable <= 80000:
        return 20000 * 0.10 + (revenu_imposable - 50000) * 0.15
    else:
        return 20000 * 0.10 + 30000 * 0.15 + (revenu_imposable - 80000) * 0.20

employes = {"Awa": 100000, "Salif": 40000}
total_net = 0

with open("bulletin.txt", "w") as f:
    f.write("===== BULLETIN =====\n")
    for nom, brut in employes.items():
        imposable = brut - brut / 10
        net = imposable - impot(imposable)
        total_net += net
        f.write(f"{nom} : net {net:.2f}\n")
    f.write(f"Total net : {total_net:.2f}\n")

print("Rapport écrit dans bulletin.txt")