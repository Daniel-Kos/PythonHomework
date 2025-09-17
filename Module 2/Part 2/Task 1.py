print("Введите число от 1 до 7")
num = int(input())

while num > 7 or num < 1:
    print("Пожалуйста, введите число от 1 до 7")
    num = int(input())

if num == 1:
    print ("Понедельник")
elif num == 2:
    print("Вторник")
elif num == 3:
    print("Среда")
elif num == 4:
    print("Четверг")
elif num == 5:
    print("Пятница")
elif num == 6:
    print("Субота")
else:
    print("Воскресенье")