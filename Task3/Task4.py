x, y = float(input("Enter two non-equal real numbers\nx: ")), float(input("y: "))

if x < y:
    a = x
    x = (a+y)/2
    y = 2*(a*y)
else:
    a = y
    y = (a+x)/2
    x = 2*(a*x)

print('x = ', x,'\ny = ', y)
