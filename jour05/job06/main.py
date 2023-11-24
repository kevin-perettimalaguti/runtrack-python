print("Combien de de marche y'a t'il ?")
x= int (input())
print("Quelle est leur taille ?")
y = int (input())

def aller_retour_toilet(x, y):
    
    trajet = (x*y*2*5*7)/100
    return trajet

trajet_wc = aller_retour_toilet(x, y)
print(f"Pour {x} marches de {y} cm, le gardien parcourt {trajet_wc} m par semaine.")
    