# check triangle is valid or not based on sides of triangle

A = int(input("Enter side a;"))
B = int(input("Enter side b:"))
c = int(input("Enter side c:"))

if (A+B>c)   and (A+c>B)  and (B+c>0) and (A>0 ) and (B>0)  and (c>0):
    print ( "triangle is valid")
else:
    print( " triangle is not valid")    
