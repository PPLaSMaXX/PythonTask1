a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))


def count_positive(*numbers):
  positive_count = 0

  for number in numbers:
    if number > 0:
      positive_count += 1

  print(f"There are {positive_count} positive numbers among the provided values.")

count_positive(a, b, c)
