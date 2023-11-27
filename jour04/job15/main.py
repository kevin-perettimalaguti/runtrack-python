#Liste des nombres de départ
nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(f" Voici ma liste initial : {nombres}")

#Création d'un fonction pour arrondir les nombres de départ au supérieur
def arrondir(nbr):
    entier = nbr//1
    decimal = nbr % 1
    if decimal >= 0.5:
        entier += 1
    return entier    

#Création d'une fonction qui fait exactement ce que fait len() 
def range_bis(liste):
    compteur = 0    
    for x in liste:       
        compteur += 1
    return compteur

#Création d'une fonction qui utilise le trie à bulle pour mettres les nombres dans l'ordre croissant
def ordre_croissant(mon_trie):
    i = range_bis(mon_trie) - 1
    while i > 0:
        j = 0
        while j < i:        
            if mon_trie[j+1] < mon_trie[j]:
                poche = mon_trie[j+1]
                mon_trie[j+1] = mon_trie[j]
                mon_trie[j] = poche                
            j += 1            
        i -= 1


#Créons un liste vierge pour stocker les nombres après toutes les étapes
liste_des_arrondies = []

#Une boucle qui parcourt chaque valeur ajoutées et leur applique la fonction qui arrondie au supérieur
for i in nombres:
    liste_des_arrondies += [arrondir(i)]

#Rappelle de la fonction "ordre croissant" puis on affiche la nouvelle liste
ordre_croissant(liste_des_arrondies)
print(f"Voici la nouvelle liste avec les chiffres/nombres arrondies : {liste_des_arrondies}")



