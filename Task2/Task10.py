N = [10, 20, 40, 30, 5, 80, 100]

#min(N)?

min_value = N[0]
for i in N:
    if i < min_value:
        min_value = i

print(min_value," position: ", N.index(min_value))
