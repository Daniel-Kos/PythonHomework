start = int(input("Number start:"))
end =  int(input("Number end:"))
seven_list = []
all_number_list = []
revers_number_list = []
reserv_list = []
five_list = []


for n in list(range(start, end)):
    n = int(n)

    reserv_list.append(n)
    revers_number_list = reserv_list[::-1]

    all_number_list.append(n)

    if n % 7 == 0:
        seven_list.append(n)

    elif n % 5 == 0:
        five_list.append(n)


print(all_number_list, revers_number_list, seven_list, five_list)