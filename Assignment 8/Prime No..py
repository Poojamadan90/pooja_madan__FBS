#sum of all prime number between 1 to n
def  Prime (num):
    sum = 0
    for x in range(1,num+1):
        for i in range(1,num):
          if( x % i ==0):
              break
    else:
        sum = sum + num   
    return sum

num = int(input("Enter Number:"))
ans = Prime (num)
print(ans)