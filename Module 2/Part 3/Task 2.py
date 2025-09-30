number = int(input('Enter a number: '))

while True:
    degree = int(input('Enter a degree: '))
    if 0<= degree <= 7:
        break
    else:
        pass

print(number ** degree)
