def pas_de_doublons(liste):
    liste_sans_gemeaux = []
    for element in liste:
        if not any(element == x for x in liste_sans_gemeaux):
            liste_sans_gemeaux = liste_sans_gemeaux + [element]
    return liste_sans_gemeaux

# Liste initiale
liste_initiale = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Supprimer les doublons
liste_sans_gemeaux = pas_de_doublons(liste_initiale)

# Afficher la liste sans doublons
print(liste_initiale)
print(liste_sans_gemeaux)