# Déclaration des variables
phrase = input("Veuillez écrire votre phrase: ")

minus=('e' in phrase)
upper=('E' in phrase)

# Comparaison et affichage du résultat

if minus or upper:
    print("Votre phrase contient le caractère e")
else:
    print("Votre phrase ne contient pas le caractère e")
