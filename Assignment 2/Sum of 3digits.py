#find sum of three digits 

num = int(input("Enter a 3 digit number:"))
    
num1= num % 10    #3
num = num//10  
num3 = num % 10
num2 = num//10 




sum = num1+ num2+ num3
print ("sum of 3 digits:",sum)