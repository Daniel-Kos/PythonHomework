start = int(input("Enter the number from which the table will begin:"))
end = int(input("Enter the number at which the table ends:"))

for i in range(start, end+1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}", end = '\t')
    print("" * 10)