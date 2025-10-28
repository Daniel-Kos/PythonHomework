summary_sheet = []

num = list(range(100, 1000))

for number in (num):
    number = str(number)
    if number[0] == number[1] or number[0] == number[2] or number[1] == number[2]:
        summary_sheet.append(number)

print(summary_sheet)
print(len(summary_sheet))