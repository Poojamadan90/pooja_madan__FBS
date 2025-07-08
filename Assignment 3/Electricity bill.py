# WAP for to input elecricity unit charges and calculate total electricity bill according to given condition 
#for first 50 units RS. 0.50/unit
#for Next 100 units RS. 0.75/unit
#for Next 100 units RS. 1.20/unit
#For unit above 250 RS.1.50/unit

units = int(input("Enter Electricity units:"))

# for first 50 units RS. 0.50/unit
if(units <= 50):
    bill = 0.5 *units 
    
elif(units > 50)  and (units <= 150):
    bill = 0.5 * 50
    units = units - 50
    bill = bill + 0.75 *units
    
    
elif( units> 150) and (units<= 250):
    bill =0.5 *50    
    units = units - 50
    bill = bill + (0.75 * units)
    units = units - 100
    bill = bill +  (units*1.20)
else:
    bill = 0.50*50
    units = units - 50
    bill += 0.75* 100          
    units = units -100
    bill += 1.20*100
    units = units - 100
    bill += 1.50*units
    
bill = bill+ (bill*0.20)   
print("bill:",bill)