#check if given number is perfect number.

num = int(input("Enter numberP:"))

sum = 0 
for i in range(1,num):
    if num % i == 0:
      sum = sum + i
if sum ==num:
    print("it is a perfect number")
else:
    print(" it is not a perfect number")
    