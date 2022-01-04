x = 0
i = int(input("Nombre entier pour la factorielle : "))
compteur = 0
factoriel = 1

for x in range(i):
    compteur = compteur + 1
    factoriel = factoriel * compteur

print(factoriel, "est le factoriel de", compteur)