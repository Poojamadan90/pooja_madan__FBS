def factors(number):
    print(f"Factors of {number}:", end=" ")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i,end=" ")
factors(12)            
    