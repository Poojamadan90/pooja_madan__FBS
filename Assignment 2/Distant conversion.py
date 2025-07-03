#convert distant given in feet and inches into meter and centimeter.

feet   = int(input("enter distant in feet:"))
inches = int(input ("enter distant in inches:"))

meter  = feet*0.3048
centimeter = inches*2.54
print("Distance in meter:", meter , "Distance in centimeter:",centimeter)