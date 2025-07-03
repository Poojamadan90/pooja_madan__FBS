#convert days into years,weeks and days.

days = int(input("Enter no. of days:"))

years = days // 365
days  = days % 365
weeks = days // 7
days  = days % 7

print("years:",years)
print("Weeks:",weeks)
print("days:",days)