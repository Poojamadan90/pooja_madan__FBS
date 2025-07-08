

age1 = int(input("Enter age of first person"))
ticket1= int(input("Enter ticket valuue for first person"))

if(age1 <= 12):
      pay_1 = ticket1*0.70
elif(age1>= 59):
     pay_1 = ticket1*0.50
else:
    pay_2 = ticket1
    
age2 = int(input("Enter age of second person"))
ticket_2= int(input("Enter ticket valuue for second person"))
if(age1 <= 12):
      pay_2 =ticket_2*0.70
elif(age1>= 59):
     pay_2= ticket_2*0.50
else:
    pay_2 = ticket_2
    
age3 = int(input("Enter age of third person"))
ticket_3= int(input("Enter ticket valuue for third person"))
if(age1 <= 12):
      pay_3 =ticket_3*0.70
elif(age1>= 59):
     pay_3= ticket_3*0.50
else:
    pay_3 = ticket_3
    

age4 = int(input("Enter age of fourth person"))
ticket_4= int(input("Enter ticket valuue for fourth person"))
if(age4 <= 12):
      pay_4 =ticket_4*0.70
elif(age1>= 59):
     pay_4= ticket_4*0.50
else:
    pay_4= ticket_4

age5 = int(input("Enter age of fifth person"))
ticket_5= int(input("Enter ticket valuue for Fifth person"))
if(age5 <= 12):
      pay_5 =ticket_5*0.70
elif(age1>= 59):
     pay_5= ticket_5*0.50
else:
    pay_5= ticket_5

total_amount = pay_1+pay_2+pay_3+pay_4+pay_5
