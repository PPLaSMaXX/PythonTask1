a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))


def count_negatives(*numbers):
  negative_count = 0

  for number in numbers:
    if number < 0:
      negative_count += 1

  print(f"There are {negative_count} negative numbers among the provided values.")

count_negatives(a, b, c)
