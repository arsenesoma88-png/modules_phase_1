N=int(input("Combien de nombre : "))
max=int(input("Saisis le nombre n°1 : "))
k=2
while k<=N:
    nombre=int(input(f"Saisis le nombre n°{k} : "))
    if nombre > max:
        max=nombre
    k=k+1
print(f"Le maximum des nombres saisis est {max}")
    