#There is a list with some numbers. Create a new
#[1,3,4,1,2,3,6,7,1,2,4]
#{1:3,3:2,2:2,

numbers = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

freq = {}   # empty dictionary

for i in range(len(numbers)):      
    num = numbers[i]              
    if num in freq:                
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1

print("Frequency Dictionary:", freq)