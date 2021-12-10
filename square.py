def square(number):
    if number==1:
        return 1
    return 2 * square(number-1)
i=1
while i<10:
    print(square(i))
    i+=1
