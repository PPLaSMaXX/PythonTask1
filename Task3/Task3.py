def is_triangle_valid(angle1, angle2):

  if angle1 <= 0 or angle2 <= 0 or angle1 + angle2 >= 180:
    return False
  return True

def is_right_triangle(angle1, angle2):

  return angle1 == 90 or angle2 == 90 or 180 - (angle1 + angle2) == 90

angle1 = float(input("Введіть перший кут (в градусах): "))
angle2 = float(input("Введіть другий кут (в градусах): "))

if not is_triangle_valid(angle1, angle2):
  print("Неможливо утворити трикутник з заданими кутами.")
  exit()

is_right = is_right_triangle(angle1, angle2)
triangle_type = "прямокутний" if is_right else "звичайний"

print(f"Даний трикутник - {triangle_type}.")
