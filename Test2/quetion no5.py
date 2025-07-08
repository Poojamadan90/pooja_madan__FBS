#A man goes for shopping. He buys 5 products. Accept the price of all products and displaythe total bill after adding 18% GST

price1 = float(input("Enter price of product 1: "))
price2 = float(input("Enter price of product 2: "))
price3 = float(input("Enter price of product 3: "))
price4 = float(input("Enter price of product 4: "))
price5 = float(input("Enter price of product 5: "))

total_price = price1 + price2 + price3 + price4 + price5

# Calculate GST (18% of total price)
gst = total_price * 0.1
total_bill = total_price + gst

print("total bill amount:",total_bill)

