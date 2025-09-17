print("Введите количество метров")
meters = float(input())

print("mili для миль \ninche для дюймов \nyard для ярдов")
action = input("")

if action == "mili":
    print(meters / 1609.344)
elif action == "inche":
    print(meters * 39.37007874015748)
elif action == "yard":
    print(meters * 1.09361)
else:
    print("Ну зачем ты это написал?")