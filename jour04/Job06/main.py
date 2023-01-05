def liste():
    L = [2, 5, 8, 11, 14]
    n = len(L)
    n = n - 1
    first = L[0]
    last = L[n]
    L[0] = last
    L[n] = first
    print(L)
liste()
