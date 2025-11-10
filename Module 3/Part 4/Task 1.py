start = int(input('Enter the start of the range:'))
end = int(input('Enter the end of the range:'))
sheet = [i for i in range(end + 1)]
complete_list = []
index = 0

if sheet[1] == 1:
    sheet[1] = 0

i = 2

while i <= end:

    if sheet[i] != 0:
        j = i + i

        while j <= end:
            sheet[j] = 0
            j = j + i
    i += 1

sheet = [i for i in sheet if i != 0]

for n in sheet:
    if n < start:
        index += 1
    elif n >= start:
        complete_list.append(sheet[index:])
        break

print(complete_list)
