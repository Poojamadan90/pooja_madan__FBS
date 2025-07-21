#Write a program to accept basic salary of n emp. (n should be
#accepted from user). If basic salary is below 20000 then
#da=10%, ta=12% and hra=15% otherwise da-15%, ta=18% and hbra=20%. Based on this calculate the total salary of each emp and also total salary of all emp

num = int(input("Enter Number of Employee:"))
total_S_of_Employee = 0
for i in range(1, num+1):
     Basic_Salary = float(input("Enter Basic_Salary of Employee"))
     if Basic_Salary< 20000:
        da = Basic_Salary * 0.10
        ta = Basic_Salary * 0.12
        hra = Basic_Salary * 0.15
        
     else:
        da = Basic_Salary * 0.15
        ta = Basic_Salary * 0.18
        hra = Basic_Salary * 0.20
        
     Total = Basic_Salary + da +ta + hra     
     print("total salary of_Employee:",Total)
     total_salary_of_employee =total_S_of_Employee + Total