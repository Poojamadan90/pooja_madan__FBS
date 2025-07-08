#Write a program to calculate the total cost of painting. The interior of building with fourequal sized walls.


height = float(input("Enter height of the wall (in meters): "))
width = float(input("Enter width of the wall (in meters): "))
cost_per_sq_meter = float(input("Enter cost of painting per square meter: "))

area_one_wall = height * width

total_area = 4 * area_one_wall

total_cost = total_area * cost_per_sq_meter

print("The total cost of painting the interior is:" ,total_cost)