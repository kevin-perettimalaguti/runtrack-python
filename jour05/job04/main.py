def carpette(n):
    
    depart = "+" + "-" * (n+1) + "+"
    print(depart)

    for y in range(n + 1):                  
        print("|" + "#" * (n-y) + " " + "#" * y + "|")           

    base = "+" + "-" * (n+1) + "+"
    print(base)


carpette(10)       
