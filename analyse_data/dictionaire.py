# Instructions
# 1. Creer un dicto des etudiants avec les cles suivants 'nom', 'age', 'notes'
# ajouter des valeurs au differents cles comme suit: nom => "Ali", age => 24 , notes = [15, 13, 18, 12]
# 2. Ajouter une nouvellle clee 'classe' avec la valeur 'Terminal'
# 3. Acceder et Afficher la valeur de la cle 'nom' et de la cle 'age'
# 4. Afficher toutes les notes 
# 5. Exo Maison calculer et retourner la moyenne des notes

etudiant = {
    "nom": "Ali", 
    "age": 24, 
    "notes": [15, 13, 18, 12]
}

# acceder au 1er element de la liste 
nom = etudiant['nom']
print(f'Bonjour je suis {nom} ')

# Ajouter une clee classe avec valeur Terminal\
etudiant['classe'] = 'Terminal'
print(f"Je suis en classe de {etudiant['classe']}")

