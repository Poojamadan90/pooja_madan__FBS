# notes pro

amount= int(input("Enter amount:"))

#500
N500 = amount // 500
r_amount = amount % 500

#200
N200 = r_amount // 200
r_amount = r_amount % 200

#100
N100 = r_amount// 100
r_amount = r_amount % 100

#50
N50 = r_amount // 50
r_amount = r_amount % 5

#20
N20 = r_amount // 20
r_amount = r_amount % 20

#10
N10 = r_amount // 10
r_amount = r_amount % 10

print("Notes To be paid for amount:",amount)
print("notes for N500:", N500)
print("notes for N200:", N200)
print("notes for N100:", N100)
print("notes for N50:", N50)
print("notes for N10:",N10)