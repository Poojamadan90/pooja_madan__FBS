#Write a program to find sum of following series using recursive functions:

#i. 1! + 2! + 3! + 4! +..... + n!

def fact(num):
    if (num==1):
        return 1
    else:
        return num*fact(num-1)
def sum_of_factorials(num):
    if num == 1:
        return 1
    return fact(num) + sum_of_factorials(num-1)    

num = int(input("Enter Number:"))  
ans = sum_of_factorials(num)
print(ans)
