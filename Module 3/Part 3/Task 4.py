number = input("Enter number:")
finaly = []

for n in number:
    n = int(n)
    if n == 3 or n == 6:
        pass
    else:
        finaly.append(n)

print(*finaly, sep='')