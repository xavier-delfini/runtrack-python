def pavé_césar(message,direc_decal):
    import string
    message=message.lower()
    alphabet = string.ascii_lowercase
    n=len(message)
    i=0
    L=list(message)
    if direc_decal == "gauche":
        i = 0
        while n>i:
            if L[i] =='a' :
                L[i] = 'x'
            elif L[i] == 'b':
                L[i] = 'y'
            elif  L[i] =='c':
                L[i] = 'z'
            elif L[i] !=" " or L[i] !="," or L[i] !=".":
                m = alphabet.find(L[i])
                if m >= 0:
                    L[i] = alphabet[m - 3]

            i+=1
        print(L)
    elif direc_decal == "droite":
        i = 0
        while n>i:
            if L[i] =='z' :
                L[i] = 'c'
            elif L[i] == 'y':
                L[i] = 'b'
            elif  L[i] =='x':
                L[i] = 'a'
            elif L[i] !=' ' or L[i] !=',' or L[i] !='.':

                m = alphabet.find(L[i])
                if m >=0:
                    L[i]=alphabet[m+3]

            i+=1
        print(L)
    else:
        print("Veuillez indiquer une direction entre gauche et droite")

pavé_césar("Salut mon pote","droite")
pavé_césar("Salut mon pote","gauche")
pavé_césar("zyx abc","droite")
pavé_césar("zyx abc","gauche")