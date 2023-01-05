def my_long_word(taille,phrase):
    phrase = "Ceci est une phrase très longue et je vais la faire très longue pour test mon programme par ce qu'au sinon ça va jamais marché"
    def compteur_list():
        n = 0
        i = 1
        while i:
            try:
                phrase[i]
                i += 1
                n += 1
            except Exception:
                break
        return n
    def comparaison_mot():
        résultat = ""
        a=0
        dumper=0
        while n >= a:
            i = dumper
            j = dumper
            while n >= i and phrase[i] != " ":
                i += 1
                taille_mot = i - j
                dumper = i + 1
            if taille_mot > taille:
                début= dumper- taille_mot -1
                fin= dumper
                résultat= résultat +phrase[début:fin]

            a=dumper

        print(résultat)
    n = compteur_list()

    comparaison_mot()



my_long_word(3,"Ceci est une phrase très longue et je vais la faire très longue pour test mon programme par ce qu'au sinon ça va jamais marché")
