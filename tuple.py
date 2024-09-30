# Un tuple en Python est une structure de données similaire à une liste,
# mais immutable (c'est-à-dire que ses éléments ne peuvent pas être modifiés une fois le tuple créé).
# Les tuples sont définis avec des parenthèses ().
#    Ordonnés : Les éléments dans un tuple ont un ordre défini.
#    Immutables : Une fois créés, leurs éléments ne peuvent pas être modifiés, ajoutés ou supprimés.
#    Les éléments peuvent être de types différents (int, str, list, etc.).

week_days_tuple = ("LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI")

print(week_days_tuple)

for weekDay in week_days_tuple:
    print(f"On est {weekDay}")


