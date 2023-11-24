L_initial = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L_tempo = []
print(L_initial)

for i in L_initial:
    if i not in L_tempo:
        L_tempo = L_tempo + [i] 


print(L_tempo)

        
