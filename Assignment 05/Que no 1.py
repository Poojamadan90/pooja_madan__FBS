#Write a program to prompt user to enter userid and password. If Id and
#password is incorrect give him chance to re-enter the credentials. Let him try 3
#times. After that program to terminate.

correct_id = "admin"
correct_password = "1234"

attempts = 3

for i in range(attempts):
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    
    if user_id == correct_id and password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Incorrect ")
else:
    print("failed attempts")

