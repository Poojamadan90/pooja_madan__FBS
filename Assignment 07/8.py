for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end=" ")
    for j in range(1,i+1):
        print(j, end = " ")   
    k = j-1     
    for j in range(1,i):
       print(k ,end = " ")
       k = k-1         
    print()