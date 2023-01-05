def liste():
    L = [8,24,48,2,16]
    n=len(L)
    i=0
    j=0
    while n>i:
        if L[i] % 3 == 0:
            j+=1
        i+=1
    print(j)
liste()
