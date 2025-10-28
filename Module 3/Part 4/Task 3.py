start = int(input("Enter the beginning of the range: "))
end = int(input("Enter the end of the range: "))

max_length = 0
for i in range(start, end + 1):
    for j in range(1, 11):
        eq_length = len(f"{i} * {j} = {i * j}")
        if eq_length > max_length:
            max_length = eq_length

for i in range(start, end + 1):
    for j in range(1, 11):
        equation = f"{i} * {j} = {i * j}"
        print(equation.ljust(max_length + 1), end='')
    print()
    if i < end:
        print()
