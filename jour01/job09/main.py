nom = "Télévision 4K HDR"
prix = 456.99
stock = 50


print (f"J'ai {stock} de {nom} qui coûtent {prix} l'unité")

print ("Combien voulez-vous en acheter ?")

demande = int (input())
stock = stock - demande
prix = (prix * 1.1)


print (f"Il reste desormais {stock} {nom} en stock. Avec la recente inflation de 10% , le prix passe à {prix}.")
