# Sets (Ensembles) :
# Un set en Python est une collection non ordonnée et non indexée d'éléments uniques. Ils sont définis avec des accolades {}.

# Caractéristiques des Sets :
# Non ordonnés : Les éléments dans un set n'ont pas d'ordre défini.
# Non indexés : Vous ne pouvez pas accéder aux éléments d'un set par leur position (comme dans une liste ou un tuple).
# Unicité : Chaque élément d'un set est unique ; les doublons ne sont pas autorisés.
# Modifiables : Vous pouvez ajouter ou supprimer des éléments d'un set.

fournitures = {"Ardoise", "Tracoire", "Craie"}

print(fournitures)

# ajout de Stylo
element4 = "Bic Schneider"
print("Apres mise a jour ")
fournitures.add(element4)
print(fournitures)

# Effacer un element
fournitures.remove("Craie")
print(f"apres effacage de Craie on a forunitures = {fournitures}")

for el in fournitures:
    print(f"{el} est inclus dans la lsite des forunitures")
