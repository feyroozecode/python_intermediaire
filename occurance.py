# Exercice 3 :
# Objectif : Compter les occurrences et rechercher un élément.
# Instruction :
# 1. Crée une liste elements contenant les éléments [1, 2, 2, 3, 3, 3, 4, 4, 4, 4].
# 2. Utilise la méthode count() pour trouver combien de fois le nombre 3 apparaît.
# 3. Utilise la méthode index() pour trouver l’index du premier élément 4.

notes = [5, 3, 4, 3, 3, 3, 7, 9]

# OCCURNCES (NOMBRE DE REPETION)
entree = input("Entree une note pour verifier sonoccurance")

occurances_de_trois = notes.count(int(entree))


print(f"L'element {entree} s' est repeter {occurances_de_trois} fois")

# touver l'index du premier element 4
index_de_quatre = notes.index(4)
print(f"Le premier element 4 est a l'index {index_de_quatre} ")
