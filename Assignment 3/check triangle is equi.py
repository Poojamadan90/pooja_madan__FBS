#check whether the triangle is Equilaterl, isosceles or scalene baed on sides

x = int(input("Enter first side :"))
y = int(input("Enter second side:"))
z = int(input("Enter third side:"))

if(x == y) and (y==z):
    print("triangle is Equilateral")
    
elif( x==y) or (y==z ) or (x==z):
    print("triangle is Iscoscels")
    
else:
    print("triangle is scalene")  
    