x, y = int(input("x: ")),int(input("y: "))
result = 0
if x > y:
    result = x - y
elif x < y:
    result = x + y
else:
    result = x

print(result)
