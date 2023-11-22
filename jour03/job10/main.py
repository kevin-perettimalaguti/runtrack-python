def number(nombre):

    if (nombre % 2) == 0 and nombre > 0 and (nombre % 1) == 0:
        print(f"Le nombre {nombre} est pair")
    
    elif (nombre % 2) != 0 and nombre > 0 and (nombre % 1) == 0:
        print(f"Le nombre {nombre} est impair")

    else:
        print ("Le nombre n'est pas entier ou positif")


number(2)
number(7)
number(0.2)
number(-2)
number(3)
number(8)


