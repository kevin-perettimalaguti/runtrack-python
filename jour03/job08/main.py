def potager(type, saison):

    if type == "fruits" and saison == "hiver":
        print ("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "ete":
        print ("Poire, fraise, cassis")

    elif type == "legume" and saison == "hiver":
        print ("carotte, topinambour, endive")

    elif type == "legume" and saison == "ete":
        print ("artichaut, aubergine, navet")

    else:
        print ("Ce n'est ni un fruit ni un légume chef")

potager("fruits","hiver")
potager("fruits","ete")
potager("legume","hiver")
potager("legume","ete")
potager("granola","ile-flotante")
