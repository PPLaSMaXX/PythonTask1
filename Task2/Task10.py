my_list = [float(input("first:")), float(input("second:")), float(input("third:")), float(input("fourth:")), float(input("fifth:")), float(input("sixth:"))]

result = 0

for i in my_list:
    if i % 5 ==0:
        result += i

print(my_list, "Sum of numbers divisible by 5:", result)
