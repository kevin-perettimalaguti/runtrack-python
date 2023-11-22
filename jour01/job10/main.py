investissement = 30000
taux = 0.08

print (f"Investissement de {investissement}€")
gain = investissement * taux
print (f"Mon gain annuel {gain}")

print (f"L'investisseur augmente son capital de 5000 euros, le taux augmenta de 2%")
investissement = investissement + gain + 5000
taux = taux + taux * 0.02

gain = investissement * taux
print (f"Gain total annuel {gain}")

print (f"L'investisseur retire 10% du montant total, suite à ca, le rendement diminue de 1%")
investissement = investissement * 0.9
taux = taux - taux * 0.01

gain = investissement * taux

investissement = investissement + gain
print (f"Le montant final de l'investissmement est {'%.2f' % investissement} et le le nouveau gain est { '%.2f' % gain}")






