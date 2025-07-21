# Write a program to calculate the sum of following series
#where n is input by user.
#1/1!+2/2!+3/3!+4/4!+...NN!

n = int(input("Enter the n:"))
fact  = 1
sum = 0

for i in range(1, n+1):
    fact = fact*i
    term = i /fact
    sum = sum + term
    
    print(sum)
    
        