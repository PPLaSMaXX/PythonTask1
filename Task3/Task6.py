a, b = int(input("a: ")), int(input("b: "))

if a == b:
    a = 0
    b = 0
else:
    a = max(a, b)
    b = a

print(a, b)
