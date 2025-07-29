#Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

num = int(input("Enter number of students:"))

for i in range(1,num+1):
    print("ENter marks of students:")
    total_marks =0
    for i in range(1,6):
        marks = int(input("subject marks:"))
        
        total_marks = total_marks + marks
    percentage = total_marks/5
    print("students  percentage",percentage)
    total_per= 0
    total_per = total_per+percentage
average = total_marks/num
print("Avg percentage of all students:", average)