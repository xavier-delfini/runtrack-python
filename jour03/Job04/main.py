def Fizzbuzz():
    i = 0
    while i < 101:
        if i % 3 == 0 and i % 5 == 0 and i != 0:
            print("FizzBuzz")
        elif i % 3 == 0 and i != 0:
            print("Fizz")
        elif i % 5 == 0 and i != 0:
            print("Buzz")
        i += 1


Fizzbuzz()