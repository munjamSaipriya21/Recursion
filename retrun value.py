def my_function(num):
    if num==5:
        return 1
    return my_function(num-1)
print(my_function(10))

# def my_function(num):
#     if num==5:
#         return 1
#     print(my_function(num-1))
# my_function(10)