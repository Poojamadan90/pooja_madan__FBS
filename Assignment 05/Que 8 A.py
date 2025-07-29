
# Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!


num = int(input("Enter Number:"))
fact = 1
sum = 0
for i in range(1,num+1):
    fact = fact * i
    sum = sum + fact
print(sum)