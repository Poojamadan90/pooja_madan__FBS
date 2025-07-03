#reverse of three digits 

num = int(input("Enter three digit no.:"))
a   = num % 10
num = num // 10
b   = num % 10
c   = num // 10

Reverse  =  (a*100 )+  (b*10) + c
print("reverse of 3 digit no:", Reverse)