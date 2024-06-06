a, b, c = (input("a: ")), (input("b: ")), (input("c: "))


def count_negatives(*numbers):
  integer_count = 0

  for number in numbers:
    try:
        int(number)
        integer_count += 1
    except ValueError:
        continue

  print(f"There are {integer_count} integer numbers among the provided values.")

count_negatives(a, b, c)
