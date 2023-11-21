
while True:
        try:
            N = int(input("Entrez un entier supérieur à zéro : "))            
            if N > 0:
                for h in range(1, N + 1):
                    print(f"La table de multiplication sera celle de {h}")
                    for i in range(1, 11):
                        print(f"{i} x {h} = {i * h}")
                break
            else:
                print("Il faut écrire un nombre entier supérieur à zéro")
        except ValueError:
            print("Veuillez entrer un nombre entier supérieur à zéro.")

