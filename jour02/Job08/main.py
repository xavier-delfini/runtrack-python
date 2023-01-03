def seasonial(type,saison):
    if type == "fruits":
        if saison == "hiver":
            print("orange,mandarine et kiwi")
        elif saison == "été":
             print("Poire,fraise,cassis")
        else:
            print("Entrée incorrecte, veuillez entrer une saison")
    elif type == "légumes":
        if saison == "hiver":
            print("carotte,topinambour,endive")
        elif saison == "été":
            print("artichaut,aubergine,navet")
        else:
            print("Entrée incorrecte, veuillez entrer une saison")
    else:
        print("Entrée incorrecte, veuillez entrée un type entre légumes et fruits")

seasonial("fruits","hiver")
seasonial("fruits","été")
seasonial("légumes","hiver")
seasonial("légumes","été")
