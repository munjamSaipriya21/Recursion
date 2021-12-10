def pal (string):
    # if string == "":  
    #     return " Palindrom"
    if len(string) == 1: 
        return "palindrom"
    elif string[0] == string[len(string)-1]:  
        return pal (string[1:][:-1])
    else:
        return "not Palindrom"
n=input("enter the string:")
print(pal(n))