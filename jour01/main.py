#Job 2
print(10+3)

#Job 4
import string
print(string.ascii_lowercase)

#Job 5
print(string.ascii_lowercase[::-1])

#Job 6
def ma_string():
    print("je suis une String")

ma_string()

#Job 7
def addition():
    num1=40
    num2=2
    print(num1+num2)

addition()

#Job 8
def produit():
    num1=3
    num2=14
    print(num1*num2)

produit()


#Pour aller plus loin

#Déclaration des variables
phrase=input("Veuillez écrire votre phrase: ")
minus=('e' in phrase)
upper=('E' in phrase)

#Comparaison et affichage du résultat
if minus or upper:
    print("Votre phrase contient le caractère e")
else:
    print("Votre phrase ne contient pas le caractère e")
