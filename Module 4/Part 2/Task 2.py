import random

number_list = [random.randint(-50,50) for _ in range(75)]
number_more_than_0 = 0
number_less_than_0 = 0
number_equal_to_0 = 0

number_max = max(number_list)
number_min = min(number_list)

for number in number_list:
    if number > 0:
        number_more_than_0 += 1
    elif number < 0:
        number_less_than_0 += 1
    elif number == 0:
        number_equal_to_0 += 1

print(f"The number of numbers equal to 0: {number_equal_to_0}\nNumber of numbers greater than 0: {number_more_than_0}\nNumber of numbers less than 0: {number_more_than_0}\nMax number: {number_max}\nMin number: {number_min}")