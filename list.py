def show_list(list):
    # parours la liste et on affiche chaque valeur avec sa position
    for index, value in enumerate(list):
        print(f"On a le fruit {value} a la position {index}")


fruits = ["Mangue", "Pomme", "Ananas", "Banane"]

print({show_list(fruits)})   

# Ajout a la liste 
fruits.append("Pasteque")

print(f"Mise a jour de la liste {fruits}")

print({show_list(fruits)})

# ajout a une position 
fruits.insert(2, "Orange")
print(fruits)

#supression dans la liste par valeur 
fruits.remove("Pomme")
print(fruits)

# supression dans la liste par index
del fruits[4]
print(fruits)

#supprimer avec la fonction pop
fruits.pop(2)

# afficher longuer de la liste
taille = len(fruits)
print(f"Taille de la liste = {taille}")