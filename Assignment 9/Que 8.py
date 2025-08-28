#Write a program to check whether a number is prime or not using recursion.
  
def prime(n, i=2):

    if n <= 1:
        return False
    if i * i > n:   
        return True
    if n % i == 0:  
        return False
    

    return prime(n, i + 1)

num = int(input("Enter a number: "))
if prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is Not a Prime Number")