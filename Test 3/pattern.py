#program to print pattern
#1 0 1 0 1 
#0 1 0 1 0 
#1 0 1 0 1
#0 1 0 1 0
#1 0 1 0 1

for i in range(1,6):
    for j in range(1,6):
        if( i+j) % 2!=0:
            print("0", end=" ")
        else:
            print("1" , end=" ")
    print( )    