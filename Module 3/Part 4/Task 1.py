start = int(input('Enter the start of the range:'))
end = int(input('Enter the end of the range:'))
final_sheet = []

for n in list(range(start, end)):
    n = int(n)
    if n == 2 or n % 2 == 1 and n >= 2:
        final_sheet.append(n)

print(final_sheet)