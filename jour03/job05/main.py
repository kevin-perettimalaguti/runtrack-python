def calcule(num1, operator, num2):   

    if operator == "+":
        return num1 + num2
    
    elif operator == "-":
        return num1 - num2
    
    elif operator == "x":
        return num1 * num2
    
    elif operator == "/":
        return num1 / num2   
    
    else:
        print("Je ne comprend pas ton opération actuelle")

resultat = calcule(23,'x', 67)
print(f"Le résultat de l'opération est {resultat}")

    



