for i in range(1,6):
    x=i
    for j in range( 1,7-i):
        if  i == 1 or  j == 1  or j == 6-i:
        
            print(x, end =" ")
        else:
            print(" ", end = " ")
        x = x+1
    print()     