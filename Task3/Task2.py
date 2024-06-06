import math


A = [float(input("x1: ")), float(input("y1: "))]
B = [float(input("x2: ")), float(input("y2: "))]

def distance_from_origin(point):

  return math.sqrt(point[0]**2 + point[1]**2)

nearest_point = A if distance_from_origin(A) < distance_from_origin(B) else B

print("Nearest point is", nearest_point)
