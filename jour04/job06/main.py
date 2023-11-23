liste = [1, 2, 3, 4, 5]
print (liste)

premier = liste[0] #Dans la poche 
liste[0] = liste[-1] #On met le 1 a la dernière position
liste[-1] = premier #On sort le 5 de la poche et on le met en première position

print(liste)


