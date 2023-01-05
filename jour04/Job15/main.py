def arrondi():
    L=[22.4, 4.0,16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
    def compteur_total():
        n = 0
        i = 1
        while i:
            try:
                L[i]
                i += 1
                n += 1
            except Exception:
                break
        return n
    n=compteur_total()
    print(n)
    i=0
    while n>=i:
        nombre_float=L[i]
        b=nombre_float // 1
        print(b//2)
        i+=1
arrondi()