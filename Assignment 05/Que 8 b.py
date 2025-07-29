#N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)


num = int(input("Enter number:"))
sum=0
for i  in range(1, num+1):
     a = num**i
     sum = sum + a
print(sum)