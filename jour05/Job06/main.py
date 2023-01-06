def notes(L):
    n=len(L)
    i=0
    while n>i:
        if L[i]>= 40:
            m=L[i]%5
            if m >=3:
                m=5-m
                L[i]=L[i]+m
        i+=1
    print(L)
notes([43,52,32,98,34.2,84.5])