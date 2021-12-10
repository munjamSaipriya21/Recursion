def sum_natural(Number):
    if Number<=1:
        return Number
    else:
        return Number+sum_natural(Number-1)
Natural_number=6
if Natural_number<0:
    print("positive Number")
else:
    print("the sumof natural number",sum_natural(Natural_number))
   
    

