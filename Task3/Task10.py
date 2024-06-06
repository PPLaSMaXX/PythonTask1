a, b, c = int(input("a: ")), int(input("b: ")), int(input("c: "))

k = int(input("Enter divisor: "))

def find_divisible_by_k(*numbers):

    result_numbers = []

    for number in numbers:
        if number % k == 0:
            result_numbers.append(number)
    return result_numbers


print("Numbers ",find_divisible_by_k(a, b, c), " is divisible by ",k)
