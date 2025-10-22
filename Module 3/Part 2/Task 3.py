while True:
    num = int(input('Enter a number:'))
    if num == 7:
        break
    elif num > 0:
        print('Number is positive')
    elif num < 0:
        print('Number is negative')
    elif num == 0:
        print('Number is equal to zero')
print('Good bye!')
