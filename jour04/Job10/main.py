def liste():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    produit=1
    for x in L:
        if x>=25 and x<=90:
            produit= produit * x
    print(produit)

liste()