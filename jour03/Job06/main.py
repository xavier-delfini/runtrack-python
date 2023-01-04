def pyramid():
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 10

    n = len(alphabet)
    i = 0
    j =3
    k=2
    while j < n:
        if i == 0:
            print(alphabet[i])
            i+=1
        else:
            print(alphabet[i:j])
            k+=1
            i= j+1
            j= i+k



pyramid()
