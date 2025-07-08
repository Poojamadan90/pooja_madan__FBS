#farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times.
#Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then 
#calculate the total cost of fencing the field.

radius = int(input("enter radius"))
length = int(input("enter lenght"))
breadth = int(input("enter breadth"))
layers =int(input("enter layrs"))
cost_per_meter = int(input("enter cost"))

halfcircle_perimeter = 3.14 *20 + 2* radius

# Rectangle remaining sides (3 sides: length + 2 breadths)
rectangular_sides = length + 2 * breadth

# Total fencing length for one layer
total_fence_length_one_layer = halfcircle_perimeter + rectangular_sides

# Total fencing length for 5 layers
totalfence_length = total_fence_length_one_layer * layers

# Total cost
total_cost = totalfence_length * cost_per_meter

# Display result
print("Total cost of fencing:", total_cost)