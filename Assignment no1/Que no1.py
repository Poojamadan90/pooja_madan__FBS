#calculate percentage of students based on marks 

sub1= int(input("enter the sub1:"))
sub2= int(input("enter the sub2:"))
sub3= int(input("enter the sub3:"))
sub4= int(input("enter the sub4:"))
sub5= int(input("enter the sub5:"))

total_marks= 500
obtainead_marks= (sub1 +sub2 +sub3 +sub4 +sub5 )
percentage=(obtainead_marks / total_marks)*100

print("percentage of students:",percentage)