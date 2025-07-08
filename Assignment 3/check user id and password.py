# progarm for promp user to enter userid and password

import random

user_id = str(input("Enter user id:"))
password = int(input("Enter password :"))

user_id = "Pooja"
password = "1234"

if (user_id == "Pooja" and password == "1234"):
     captcha = random.randint(1000,9999)
     print("captcha")  
     user_captcha = int(input("Enter captcha"))  
     print("login saccesfulyy!")
else:
    print("failed)")
    