# ckeck given number is palindrome number or not

Num = int(input("Enter Number:"))

First_Number   = Num % 10      #1
num = Num // 10     # 12
first_number = num % 10      #2
last_number   = num // 10     #1



if First_Number == last_number:
       print("number is  palindrome number")
elif 999> Num<100:
    print(" invalid number")
else:
    print("number is  not palindromr number")
 



