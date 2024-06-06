fib1 = 0
fib2 = 1
fibonacci_range = [fib1, fib2]
print(fib1)
print(fib2)

start_index = 5
end_index = 21

i = 0

while i < end_index:
    fib_sum = fib1 + fib2

    print(fib_sum)


    fib1 = fib2
    fib2 = fib_sum

    fibonacci_range.append(fib_sum)
    i += 1

print("\nFibonacci numbers from 5 to 20:")
print(fibonacci_range[4:19],'\n\n')

j = 0
while j <= 20:
    if j % 2 == 0:
        print(j)
    j += 1

print('\n\n')

k = -1
while k >= -21:
    if k % 3 == 0:
        print(k)
    k -= 1
