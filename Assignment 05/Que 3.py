#Accept no. of passengers from user and per ticket cost. Then accept age of each
#passenger and then calculate total amount to ticket to travel for all of them based on
#following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

n =  int(input("Enter Number of passenger:"))
ticket_cost= int(input("Enter ticket cost"))

total_amount= 0

for i in range(1,n+1):
    age= int(input("Enter age of passenger:"))
    if age<12:
        fare= ticket_cost*0.70
    elif age> 59:
        fare= ticket_cost*0.50   
    else:
        fare= ticket_cost
    total_amount = total_amount+fare
        
    print(fare)
print(total_amount)    