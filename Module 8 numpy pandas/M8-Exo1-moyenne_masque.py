import numpy as np

notes = np.array([12, 8, 15, 18, 6])
longueur = len(notes)
masque = notes[notes >= 10]
moyenne_masque = masque.mean()

print("notes : ", notes)
print("moyenne des notes supérieures ou égales à 10 : ", moyenne_masque)

