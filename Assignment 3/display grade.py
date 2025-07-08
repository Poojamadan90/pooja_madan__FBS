#input five subjects marks foem user and display grade

sub1 = int(input("Enter first subject marks:"))
sub2 = int(input("Enter second subject marks:"))
sub3 = int(input("Enter third subject marks:"))
sub4 = int(input("Enter fourth subject marks:"))
sub5 = int(input("Enter fifth subject marks:"))

Total_marks = sub1 = sub2 = sub3 = sub4 = sub5
per = Total_marks /5


if( per>= 80 and per <=100 ):
    print("first class with distinction")
elif( per >=70 and per<80 ):
    print("First class")
elif( per >= 60 and per<70):
    print("higher second class")
elif ("per >= 40 and per<60"):
    print("second class")
elif("per<40 and per>0"):
    print("fail")
else:
    print("wrong input")