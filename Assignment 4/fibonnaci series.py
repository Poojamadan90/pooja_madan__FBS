# print fibonnaci series

num = int(input("Enter number:"))

a = 0
b = 1
for i in range(num):
    c = a+b
    a = b
    b = c
    print(a)