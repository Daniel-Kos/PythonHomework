start = int(input("Number start:"))
end =  int(input("Number end:"))
number_list = []


for n in list(range(start, end)):
    if n % 7 == 0:
        number_list.append(n)

print(number_list)