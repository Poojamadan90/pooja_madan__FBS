#Write a program to find factorial using recursion.

def fact(num):
    if (num==1):
        return 1
    else:
        return num*fact(num-1)
    
num = int(input("Enter number:"))
ans = fact(num)    
print(ans)