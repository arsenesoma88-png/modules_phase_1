import numpy as np
tab = np.array([5, 12, 7, 20, 3, 15])
masque = tab > 10
filtre = tab[masque]

print("Tableau : ", tab)
print("filtre des éléments supérieur à 10 : ", masque)
print("Nombre d'éléments supérieurs à 10 : ", len(masque))

