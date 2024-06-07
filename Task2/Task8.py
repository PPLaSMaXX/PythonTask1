# def box_through_door(box:list, door:list):

#     box.sort()
#     door.sort()
#     if box[0] < door[0] and box[1] < door[1]:
#         return True
#     else:
#         return False


# box = [int(input("Write Box dimensions divided by Enter (A <Enter> B <Enter> C)\nA: ")),int(input("B: ")),int(input("C: "))]

# print(box)

# door = [int(input("Write Door dimensions divided by Enter (A <Enter> B)\nA: ")),int(input("B: "))]

# print(door)

# if box_through_door(box, door):
#     print("Коробка пройде через двері.")
# else:
#     print("Коробка не пройде через двері.")


my_list = [float(input("x:")), float(input("y:")), float(input("k:"))]


d = max(my_list)
s = min(my_list)


