# find  Area and perimeter

length = int(input("Enter length:"))
breadth = int (input("Enter breadth:"))


radius = breadth/2
area_rectangle = length*breadth
area_semicircle = (0.5*3.14*radius*radius)
total_area =  area_rectangle+area_semicircle

perimeter =  (2*length) + breadth*(0.5*3.14*radius*radius) 

print("area of figure:", total_area)
print("perimeter of figure:",perimeter )

