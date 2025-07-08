Angle_A = int(input("Enter angle of triangle A:"))
Angle_B = int(input("Enter angle of triangle B:"))
Angle_c= int(input("Enter angle of triangle C :"))

if Angle_A>0  and  Angle_B>0  and Angle_c>0  and  (Angle_c+Angle_A+Angle_B==180 ):
    print ("Traingle is valid")
else :
    print("tringle is not valid")    