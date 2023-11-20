investissement = 30000
rendement = 0.08

print (f"Investissement de {investissement}€")
gain = investissement * rendement
print (f"Mon gain annuel {gain}")

print (f"L'investisseur augmente son capital de 5000 euros, le taux augmenta de 2%")
rendement = rendement + 0.02
investissement = investissement + 5000
gain = investissement * rendement
print (f"Gain total annuel {gain}")

print ("L'investisseur retire 10% du montant total, suite à ca, le rendement diminue de 1%")
rendement = rendement - 0.01
investissement = (investissement) * 0.9
gain = investissement * rendement
print (f"Suite au retrait de 10% le montant total passe à {'%.2f' % gain}")





