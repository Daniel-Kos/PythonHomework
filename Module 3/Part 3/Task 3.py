summary_sheet = []

num = list(range(100, 10000))

for number in (num):
    if len(set(str(number))) == len(str(number)):
        summary_sheet.append(number)

print(summary_sheet)
print(len(summary_sheet))