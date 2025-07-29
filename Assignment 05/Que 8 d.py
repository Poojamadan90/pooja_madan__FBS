#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10

a = float(input("Enter number:"))
sum= 0  
for i in range(1, 11):
    ans =(a**i)/i
    sum = sum + ans   
print(sum)