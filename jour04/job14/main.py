def len_bis(lettres):
    compteur = 0    
    for x in lettres:        
        compteur += 1
    return compteur

def decouper_chaine(nb_lettre, phrase):
    decoupe = []
    debut = 0
    longueur_chaine = len_bis(phrase)
    nouvelle_phrase =""
    i=0

    while i < longueur_chaine:
        if phrase[i] == " " or phrase[i] == ",":
            decoupe += [phrase[debut:i]]
            debut = i+1
        i+=1
    decoupe += [phrase[debut:]]    

    for i in decoupe:
        if len_bis(i) > nb_lettre:
            nouvelle_phrase += i + " "
    return nouvelle_phrase
 
print(decouper_chaine(3," La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))



    











