real_numbers = [float(input("x: ")), float(input("y: ")), float(input("c: "))]

for i in real_numbers:
    if i > 0:
        print(i**3)
    elif i < 0:
        print(i**4)
