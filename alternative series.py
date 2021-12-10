def pattern(number):
    if number == 1:
        print(number)
        return 10
    elif number % 2 == 0:
        return pattern(number - 1) + 1
    
    else:
        return pattern(number - 2) * 10
print(pattern(10))