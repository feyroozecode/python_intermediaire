# Exercice 2 : Vérifier la parité des nombres
# Objectif :Vérifier si les nombres dans une liste sont pairs ou impairs en utilisant une boucle for et if.

# Instructions :
# Créez une liste nombres contenant les éléments [12, 7, 5, 19, 21, 32, 14].
# Parcourez la liste avec une boucle for et utilisez une condition if pour
# vérifier si chaque nombre est pair ou impair.
# Affichez chaque nombre avec son statut ("pair" ou "impair").

nombres = [12, 7, 5, 19, 21, 32, 14]

l_pair = []
l_impair = []

for nbr in nombres:
    if nbr % 2 == 0:
        l_pair.append(nbr)
        print(f"Le nombre {nbr} Nombre Pair")
    else:
        l_impair.append(nbr)
        print(f"Le nombre {nbr} Nombre impair")

print(f"Les pairs : {l_pair}")
print(f"Les impairs : {l_impair}")
