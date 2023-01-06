def meli_memo():
    import string
    mot=input("Veuillez renseignez un mot:")
    alphabet = string.ascii_lowercase
    liste=list(mot)
    n=len(mot)

    #Convertir le mot en nombre via l'utilisation de la base 26
    def calcul_mot(valeur):
        i=0
        résultat=0
        while n>i:
            dump = alphabet.find(valeur[i])+1
            résultat=dump * (26 ** i) + résultat
            i+=1
        return résultat
    def test_mots():
        j=0





    print(calcul_mot(mot))

meli_memo()



