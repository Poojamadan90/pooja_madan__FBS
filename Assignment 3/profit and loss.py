# calculate profit and loss

cost_price = int(input("Enter purchase cost price:"))
selling_price = int(input("Enter selling price:"))

profit = selling_price - cost_price 
loss  = cost_price - selling_price




if(selling_price > cost_price ):
    print("profit:", profit)
    
elif(cost_price > selling_price):
    print("loss:",loss)
else:
    print("no prifit, no loss")
         

