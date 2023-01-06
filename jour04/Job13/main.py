def liste():
    L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

    def compteur():
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

    n = compteur()
    j = 1
    while j <= n:
        i = 0
        while i <= n:
            print("i")
            print(i)
            print("n")
            print(n)
            if i != j and L[i] == L[j]:
                del L[j]
                n = compteur()

            i += 1
        j += 1
    print(L)


liste()
