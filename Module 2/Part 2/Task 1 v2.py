import calendar

print("Введите число от 0 до 6")
num = int(input())

name = calendar.day_name[num]

print(name)
