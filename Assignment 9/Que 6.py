#Write a program to print Fibonacci series using recursion.
def fibbo(a,b,num):
    if num>0: 
        c= a+b
        print(c)
        return fibbo(b,c,num-1)
    
num= int(input("ENter Number:"))
ans = fibbo(-1,1,num)