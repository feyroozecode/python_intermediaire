# On donne la lliste de ces participant
# parcourir la liste et afficher une salutation a chaque utilsateur
# Utiliser Salam Aleykoum Mr pour les masculin et Salam Mme [nom] pour les femmes
# Afficher enfin leur ages respective

parts = [
    ["Ali", 18, "M"],
    ["Mariama", 42, "F"],
    ["Moussa", 25, "M"],
    ["Fatouma", 15, "F"],
]

# parcours de la liste pour saluer par genre
for part in parts:
    name, age, genre = part

    if genre == "M":
        print(f"Salam aleykoum Mr {name} vous etes agee de {age}")
    else:
        print(f"Salam Aleykoum Mme {name} agee de {age}")
