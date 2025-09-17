print("Введите два числа")
number1 = int(input())
number2 = int(input())

if number1 == number2:
    print("Числа равны")
else:
    number_list = [number1, number2]
    number_list.sort()
    print(number_list)