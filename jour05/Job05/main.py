def marche(numb_marches,hauteur):
    résultat=(hauteur*numb_marches)*70/100
    print("Pour",numb_marches,"marches de",hauteur,"cm,le gardien parcours",résultat,"m par semaine")

#S'il parcours 1cm par trajet aller sachant qu'il va au toilettes 5 fois par jours ce qui nous fait 35 fois par jours multiplions
#le tout par 2 pour obtenir les trajets allés retour combiné puis divisons par 100 pour avoir la valeur en mètres
marche(1,1)

marche(100,10)
