L_initial = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
L_tempo = []
print(L_initial)

# i parcour ma liste de départ
for i in L_initial:
    #Si mon i trouve pas de nombre dans ma liste temporaire, il le rajoute
    if i not in L_tempo:
        L_tempo = L_tempo + [i] 

#Affichons la liste sans doublons maintenant
print(L_tempo)

        
