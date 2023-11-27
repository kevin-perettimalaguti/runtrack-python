def evaluer(liste_notes):
    notes_arrondies = []

    for note in liste_notes:
        # Vérifie si l'écolier a réussi le test
        if note > 40:              
            # Calcule le prochain multiple de 5 supérieur
            multiple_de_5 = ((note + 4) // 5) * 5 
            
            # Vérifie si l'arrondi est nécessaire
            if multiple_de_5 - note < 3:  
                notes_arrondies.append(multiple_de_5)  # Ajoute la note arrondie
            else:
                notes_arrondies.append(note)  # Garde la note telle quelle
        else:
            notes_arrondies.append(note)  # Garde la note telle quelle
           
    return notes_arrondies

# Exemple d'utilisation de la fonction

notes = [84, 33, 82, 63]
notes_arrondies = evaluer(notes)    
print(f"Notes initial : {notes}")
print(f"Notes arrondies : {notes_arrondies}")          










