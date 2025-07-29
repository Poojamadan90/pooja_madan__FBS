# check if a given number is prime number or not.

num = int(input("Enter number:"))

for i in range( 2,num):
    if num % 10 ==0:
        print("no, it is not prime Number")
        break
else:
      print( "yes, it is prime number")        