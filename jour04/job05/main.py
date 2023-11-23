L = [1, 2, 3, 4, 5]
print (L)
print(L[1])

def remplace(number):
    return number[3] == number[2] + number[4]

remplace(L)
print(L)
print(L[len(L)-1])