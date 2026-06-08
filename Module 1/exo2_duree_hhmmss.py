total = int(input("Nombre de secondes : "))
heures=total//3600
minutes=(total-heures*3600)//60
secondes=(total-heures*3600)%60
print(f"{total} secondes correspond à {heures} heures {minutes} minutes {secondes} secondes")
