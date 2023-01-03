import math
#Si ABC est un triangle rectangle en A, alors BC² = AB² + AC².
#BC²= AB² +AC²   = 23,04 + 4 =27,04
#AB=4,8 cm  AB²=23,04
#BC=5,2
#AC=2cm     AC²=4

#def triangle(AB,BC,AC):

def rectangle(AB,BC,AC):
    AB2= AB*AB
    BC2= BC*BC
    AC2= AC*AC
    BC_AC= BC2 + AC2
    AB_AC= AB2 + AC2
    AB_BC= AB2 + BC2
    if math.isclose(BC_AC,AB2,abs_tol =0.01):
        return("Rectangle en C")
    elif math.isclose(AB_AC,BC2,abs_tol =0.01):
        return("Rectangle en A")
    elif math.isclose(AB_BC,AC,abs_tol =0.01):
        return("Rectangle en B")

    else:
        return("Pas Rectangle")
print(rectangle(4.8,5.2,2))
print(rectangle(4,4,4))
