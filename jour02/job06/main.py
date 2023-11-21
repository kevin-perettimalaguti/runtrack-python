for ne in range(1001):

    if all(ne % i != 0 
        for i in range(2, int(ne**0.5) + 1)):
            print(ne)