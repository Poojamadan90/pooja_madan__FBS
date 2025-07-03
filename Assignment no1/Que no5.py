#calculate compound intrest

principle = float(input("Enter the principle amount:"))
Rate = float(input("Enter the Rate of interest:"))
Time = float(input("Enter the Time:"))

compound_interest = principle*(1+Rate)**Time
print("compound_interest :",compound_interest )