x = float(input("Enter the x-coordinate of point A: "))
y = float(input("Enter the y-coordinate of point A: "))

if x == 0 and y == 0:
    print("Point A is located at the origin.")
elif x == 0:
    print("Point A is located on the y-axis.")
elif y == 0:
    print("Point A is located on the x-axis.")
else:
    if x > 0 and y > 0:
        print("Point A is located in Quadrant I.")
    elif x < 0 and y > 0:
        print("Point A is located in Quadrant II.")
    elif x < 0 and y < 0:
        print("Point A is located in Quadrant III.")
    else:
        print("Point A is located in Quadrant IV.")
