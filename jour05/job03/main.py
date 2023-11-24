hauteur_triangle = int(input("Choisissez une valeur pour votre triangle : "))

def triangle(hauteur_triangle):
    
    for i in range(hauteur_triangle - 1):
        espace = " " * (hauteur_triangle - i - 1)
        
        if i == 0:
            print(espace + "/\\")
        
        else:
            print(espace + "/" + " " * (2 * i) + "\\")

    trait = "/" + "_" * (2 * hauteur_triangle - 2 ) + "\\"
    print(trait)


triangle(hauteur_triangle)

     

