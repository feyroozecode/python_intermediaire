# 1. Créer la matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2. Afficher le deuxième élément de la première liste
print(f"Le deuxième élément de la première liste est {matrice[0][1]}.")

# 3. Remplacer le nombre 6 par 60
matrice[1][2] = 60

# 4. Afficher la matrice modifiée
print("La matrice modifiée est :")
for ligne in matrice:
    print(ligne)


# Renverser laes ligne de la lsite
for ligne in matrice:
    ligne.reverse()

print("Mise a jour :: Liste inverser")
for ligne in matrice:
    print(ligne)
