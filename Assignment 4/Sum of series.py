# print sum of series upto n.

num = int(input("Enter Number:"))
sum = 0

for i in range(1, num+1):
    sum = sum + i

print("sum of series:", sum)