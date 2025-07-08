#Write a program to accept 3 digit number, If first digit is double of second digit and half of third digit then displan'"Yes, you have done it', otherwise display "Please try next time”",

num = int(input("Enter three digit no:"))

first_digit   = num % 10
num = num // 10
second_digit   = num % 10
third_digit   = num // 10

if (first_digit == 2*second_digit ) and (first_digit *2 == third_digit):
    print("yes,you have done it")
    print("please try next time")
          

