def inverse(phrase):
    #On mesure la longueur de la phrase
    n=len(phrase)
    #On converti notre chaine de caractère en list
    liste = list(phrase)
    #On déclare nos variables relative a la boucle
    i=0
    m=n-1
    #On prérempli la liste qui nous servira a stocker notre mot inversé
    inv_phrase = [None] * n
   #Tant que toutes les lettres ne sont pas traité
    while i <= n-1:
        #On prend la dernière lettre non traité et on la met a la suite
        inv_phrase[i] = liste[m]
        #On incrémente nos variables
        m-=1
        i+=1
    #On converti nos 
    inv_phrase=''.join(inv_phrase)
    print(inv_phrase)

inverse("je suis une phrase")
inverse("coucou")

