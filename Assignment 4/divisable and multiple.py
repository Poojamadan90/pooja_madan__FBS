#find all numbers in a range divisible by 7 and multiple by 5 in a given range.

start = int(input("Enter start Number:"))
stop = int(input("Enter stop Number"))

for i in range(start, stop+1):
    if i % 7 ==0  and i % 5 ==0:
        print(i)