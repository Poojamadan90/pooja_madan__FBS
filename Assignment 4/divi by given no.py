
#print all numbers in a range divisible by a given number.

divisor = int(input("Enter the number to divide by: "))   
Num = int(input("Enter the end of range: "))       



for i in range(1, Num + 1):
    if i % divisor == 0:
        print(i)

        