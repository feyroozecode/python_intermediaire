# Exercice supplémentaire : Analyser les données d'âges d'une campagne
# Objectif : Analyser et manipuler des listes de données.

# Instructions :
# Créez une liste ages contenant les âges des participants à une campagne : [23, 45, 34, 21, 56, 40, 18, 29, 37, 50].
# Affichez l'âge minimum et maximum de la liste.
# Calculez la moyenne des âges.
# Triez les âges par ordre croissant.

# Liste des âges
ages = [23, 45, 34, 21, 56, 40, 18, 29, 37, 50]

# Initialiser les variables pour l'âge minimum, maximum, et la somme des âges
min_age = ages[0]
max_age = ages[0]
somme_ages = 0

# Parcourir la liste des âges
for age in ages:
    # Trouver l'âge minimum
    if age < min_age:
        min_age = age

    # Trouver l'âge maximum
    if age > max_age:
        max_age = age

    # Ajouter l'âge actuel à la somme des âges
    somme_ages += age

# Calculer la moyenne des âges
moyenne_age = somme_ages / len(ages)

# Afficher les résultats
print(f"L'âge minimum est {min_age}")
print(f"L'âge maximum est {max_age}")
print(f"La moyenne des âges est {moyenne_age:.2f} ans")
