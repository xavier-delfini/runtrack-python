def tapis(taille):
    updown="+"
    middle="|"
    i=0
    while taille >= i and taille > 2:
        updown = updown + "-"
        i += 1
    updown = updown + "+"
    print(updown)
    j=0
    while taille >=j and taille >2:
        middle= middle +"#"
        j+=1
    k=taille+2
    middle=middle+"|"
    while k >=3 and taille >2:

        spaced=list(middle)
        spaced[k-2]=" "
        spaced=''.join(spaced)
        print(spaced)
        k-=1
    print(updown)
tapis(3)