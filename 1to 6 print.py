# def my_function(num):
#     if num==5:
#         return 1
#     else:
#         a=1+my_function(num-1)
#         print(a)
#         return a
# my_function(10)


def my_function(num):
    if num==5:
        return 1
    else:
        a=1+my_function(num-1)
        print(a)
        return a
print(my_function(10))


