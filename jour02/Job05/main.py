def calcule(num1,operator,num2):
    match operator:
        case "+":
            resultat=num1 + num2
            return resultat
        case "-":
            resultat=num1 - num2
            return resultat
        case "*":
            resultat=num1 * num2
            return resultat
        case "/":
            resultat=num1 / num2
            return resultat

print(calcule(50,"+",3))
print(calcule(50,"-",3))
print(calcule(3,"*",3))
print(calcule(50,"/",3))