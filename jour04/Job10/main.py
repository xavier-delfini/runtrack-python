def liste():
    L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
    n = len(L)
    i=0
    produit=1
    while n > i:
        if L[i]>=25 and L[i]<=90:
            produit= produit * L[i]
        i+=1
    print(produit)

liste()