import calendar

print("Введите номер месяца")
num = int(input())

while num > 12 or num < 1:
    print("Пожалуйста, введите число от 1 до 12")
    num = int(input())

month_name = calendar.month_name[num]
print(month_name)