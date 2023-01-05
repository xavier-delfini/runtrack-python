def liste(l):
    j = 0
    k = 2
    while k > j:
        i = 0
        while l[i]:
            k = 2

            temp1 = l[i]
            try:
                temp2 = l[i + 1]
                if temp1 > temp2:
                    l[i] = temp2
                    l[i + 1] = temp1
            except Exception:
                break

            i += 1
            k += 1
        j += 1
    print(l)


liste([9, 8, 3, 6, 82, 12, 81, 42, 83, 53, 82])
liste([3, 7, 1, 3, 8, 12])
