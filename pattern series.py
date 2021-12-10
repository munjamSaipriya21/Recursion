def pattern(number):
    if number == 1:
        print(number)
        return 1
    else:
        a=1+pattern(number-1)+2
        print(a)
        return a
pattern(10)