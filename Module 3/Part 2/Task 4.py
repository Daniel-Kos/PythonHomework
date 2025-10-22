num = 0
num_list = []

while True:
    num = int(input())
    if num == 7:
        break
    else:
        num_list.append(num)
    print(f"Sum of numbers:{sum(num_list)}, minimum of numbers:{min(num_list)}, maximum of numbers:{max(num_list)}")
print("Good bye!")