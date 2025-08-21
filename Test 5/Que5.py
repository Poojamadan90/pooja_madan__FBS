#Python Program to Find the Union of two Lists without
#using set concept.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

u_list = []   


for i in range(len(list1)):
    u_list.append(list1[i])


for j in range(len(list2)):
    if list2[j] not in u_list:
        u_list.append(list2[j])

print("Union of two lists:", u_list)