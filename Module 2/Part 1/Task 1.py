print("Введите 3 числа")
number1 = float(input())
number2 = float(input())
number3 = float(input())
print("Введите + для суммы\nВведите * для произведения")
action = input("")
if action == "+":
    print(number1 + number2 + number3)
elif action == "*":
    print(number1 * number2 * number3)
else:
    print("Ну зачем ты это написал?")
