#Write a program to find sum of digits using recursion.

def Sum_Of_Digits(num):
    if(num==0):
        return 0
    else:
      a= num % 10   
    return a+ Sum_Of_Digits(num//10)
num = int(input("Enter number:"))
x = Sum_Of_Digits(num)
print(x)