#print first n prime numbers
n = int(input("Enter Number:"))

for x in range(1,n+1):
    for i in range(2, x):
        if x % i == 0:
            break
    else:
      print(x)       


