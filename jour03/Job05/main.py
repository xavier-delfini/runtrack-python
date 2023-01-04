def premier():
    i = 3
    while i < 1001:
        def calcul():
            j = 2
            prim = 1
            while i > j:
                if i % j == 0:
                    prim = 0
                j += 1
            if prim == 1:
                print(i)

        calcul()
        i += 1


premier()
