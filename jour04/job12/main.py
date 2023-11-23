triage = [5, 8, 2, 15, 7, 10]

def range_bis(liste):
    compteur = 0
    # lst_range = []
    for x in liste:
        # lst_range[compteur:] = compteur
        compteur += 1
    return compteur

def ordre_croissant(mon_trie):
    i = range_bis(mon_trie) - 1
    while i > 0:
        j = 0
        while j < i:        
            if mon_trie[j+1] < mon_trie[j]:
                poche = mon_trie[j+1]
                mon_trie[j+1] = mon_trie[j]
                mon_trie[j] = poche
                #mon_trie[j+1],mon_trie[j] = mon_trie[j], mon_trie[j+1]
            j += 1            
        i -= 1

print(triage)
ordre_croissant(triage)
print(triage)




        

    

        


















    
    