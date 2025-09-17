print("Введите 3 числа")
number1 = float(input())
number2 = float(input())
number3 = float(input())

print("max для максимума \nmin для минимального \naref для среднеарефметического")
action = input("")

if action == "max":
    print(max(number1, number2, number3))
elif action == "min":
    print(min(number1, number2, number3))
elif action == "aref":
    print((number1 + number2 + number3) / 3)
else:
    print("Ну зачем ты это написал?")