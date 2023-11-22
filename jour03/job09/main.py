def moyenne(note1, note2, note3):
    return (note1 + note2 + note3) / 3

note1 = int (input("Rentrer votre première note:"))
note2 = int (input("Rentez votre deuxième note:"))
note3 = int (input("Rentrez votre troisième note:"))

moyenne_etudiant = moyenne(note1, note2, note3)

print(f"Si les notes sont {note1}, {note2}, {note3} alors la moyenne est de {'%0.f' % moyenne_etudiant}/20")

if 15 <= moyenne_etudiant <= 20:
    print ("Très bon élève")

if 11 <= moyenne_etudiant <= 14:
    print ("Bon élève")

if 8 <= moyenne_etudiant <= 10:
    print ("Élève moyen")

if 0 <= moyenne_etudiant <= 7:
    print ("Élève devant faire des efforts")








