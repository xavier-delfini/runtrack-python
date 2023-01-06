def draw_rectangle(width,height):
    i = 0
    updown = "|"
    middle = "|"
    while width - 3 >= i and width > 2:
        updown = updown + "-"
        i += 1
    updown = updown + "|"
    print(updown)
    if height >2:
        j=0
        while width -3 >=j and width >2:
            middle = middle + " "
            j+=1
        middle = middle + "|"

        k=0
        while height -2>k:
            print(middle)
            k+=1
    print(updown)






draw_rectangle(15,2)
draw_rectangle(18,12)
draw_rectangle(4,3)
