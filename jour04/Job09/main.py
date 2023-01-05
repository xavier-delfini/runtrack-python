def liste():
    L = [8,24,27,48,2,16,9,102,7,84,91]
    n=len(L)
    i=0
    min= L[0]
    max=0
    while n > i:
        if min > L[i] and max < L[i]:
            min= L[i]
            max= L[i]
        elif min > L[i]:
            min = L[i]
        elif max < L[i]:
            max = L[i]
        i+=1
    print(min)
    print(max)

liste()