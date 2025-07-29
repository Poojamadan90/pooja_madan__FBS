# print aarmstron number in given range

Start = int(input("Enter Start number: "))
Stop = int(input("Enter Stop number: "))

for i in range(Start, Stop + 1):
    temp = i
    count = 0
    sum = 0
    num = i

    
    while num != 0:
        num = num // 10
        count += 1

    num = i 
    
    while num != 0:
        a = num % 10
        sum = sum + (a ** count)
        num = num // 10

    if sum == temp:
        print(temp)

