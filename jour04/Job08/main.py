def liste():
    L = [8,24,27,48,2,16,9,7,84,91]
    n=len(L)
    i=0
    j=0
    while n>i:
        if L[i] % 2 == 0:
            j=j+L[i]

        i+=1
    print(j)
liste()