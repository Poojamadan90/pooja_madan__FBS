#Write a program to print first n prime numbers.

num = int(input("Enter number:"))
for i in range(2,num+1):
        if (num% i== 0):
            break
        else:
           print(i)  