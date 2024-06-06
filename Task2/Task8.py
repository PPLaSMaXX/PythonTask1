def box_through_door(box:list, door:list):

    box.sort()
    door.sort()
    if box[0] < door[0] and box[1] < door[1]:
        return True
    else:
        return False


box = [int(input("Write Box dimensions divided by Enter (A <Enter> B <Enter> C) ")),int(input(" ")),int(input(" "))]

print(box)

door = [int(input("Write Door dimensions divided by Enter (A <Enter> B) ")),int(input(" "))]

print(door)

if box_through_door(box, door):
    print("Коробка пройде через двері.")
else:
    print("Коробка не пройде через двері.")

