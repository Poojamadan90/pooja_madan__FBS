#Write a program to find sum of n numbers using recursion.

def sum_of_Numbres(Num):
       if (Num==1):
           return 1
       else:
          return Num+sum_of_Numbres(Num-1)
Num = int(input("Enter Number:"))       
ans= sum_of_Numbres(Num)
print(ans)
