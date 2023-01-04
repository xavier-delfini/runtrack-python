import math


# Si ABC est un triangle rectangle en A, alors BC² = AB² + AC².
# BC²= AB² +AC²   = 23,04 + 4 =27,04
# AB=4,8 cm  AB²=23,04
# BC=5,2
# AC=2cm     AC²=4
def triangle(AB, BC, AC):
    if (AB > 0) and (BC > 0) and (AC > 0):

        def rectangle(AB, BC, AC):

            # Calcul au carré
            AB2 = AB * AB
            BC2 = BC * BC
            AC2 = AC * AC

            # Calculs pour comparaison avec l'hypothénuse
            BC_AC = BC2 + AC2
            AB_AC = AB2 + AC2
            AB_BC = AB2 + BC2

            # Application du théorème de pythagore avec comparaison approximative pour contourner les problèmes de float
            if math.isclose(BC_AC, AB2):
                # Rectangle en C
                return 1
            elif math.isclose(AB_AC, BC2):
                # Rectangle en A
                return 2
            elif math.isclose(AB_BC, AC2):
                # Rectangle en B
                return 3
            else:
                # Non Rectangle
                return 0

        # Vérif si Equilatéral, isocèle ou non
        def equiso(AB, BC, AC):
            if AB == BC and BC == AC:
                # Equilatéral
                return 1
            elif AB == BC or BC == AC or AB == AC:
                # Isocèle
                return 2
            else:
                # Aucun cotés équivalents
                return 0

        # Récupération des retour de fonction
        résultat_rec = rectangle(AB, BC, AC)
        résultat_equiso = equiso(AB, BC, AC)

        #
        if résultat_rec == 0 and résultat_equiso == 1:
            print("Ce triangle est un triangle équilatéral")
        elif résultat_rec > 0 and résultat_equiso == 2:
            print("Ce triangle est un triangle isocèle rectangle")
        elif résultat_rec == 0 and résultat_equiso == 2:
            print("Ce triangle est un triangle isocèle")
        elif résultat_rec > 0 and résultat_equiso == 0:
            print("Ce triangle est un triangle rectangle")
        elif résultat_rec == 0 and résultat_equiso == 0:
            print("Ce triangle est un triangle quelquonque")
        else:
            print("Une erreur est survenue")
    else:
        print("Votre triangle n'est pas possible")


# Isocèle rectangle
triangle(6, 6, 8.485281374249)

# Isocèle
triangle(3.6, 3.6, 5)

# Quelquonque
triangle(3, 4, 6)

# Equilatéral
triangle(3, 3, 3)

# Rectangle
triangle(4.8, 5.2, 2)

# Triangle impossible
triangle(-3, -5, 3)
