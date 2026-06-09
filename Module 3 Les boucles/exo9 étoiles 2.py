while True:
    N = int(input("Saisis un nombre entier : "))
    if N >= 1:
        break
for i in range(1, N + 1):
    for k in range(i):
        print("*", end="")
    print("")