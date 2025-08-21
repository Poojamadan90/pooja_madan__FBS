#A list contains sublist with Emp information as follows :
#Data = [[101,”Seema”,45000],[340,”Rajani”,13000],
#[210,”Tannu”,14000],[320,”Suresh”,35000]]
#Write a program to sort the list based on salary.


Data = [[101, "Seema", 45000],[340, "Rajani", 13000],[210, "Tannu", 14000],
         [320, "Suresh", 35000]]
    

for i in range(len(Data)):
    for j in range(i+1, len(Data)):
        if Data[i][2] > Data[j][2]:   
            Data[i], Data[j] = Data[j], Data[i]   # swap

#  sorted list
print("Employees sorted by salary:")
for i in range(len(Data)):
    print("ID:", Data[i][0], "Name:", Data[i][1], "Salary:", Data[i][2])