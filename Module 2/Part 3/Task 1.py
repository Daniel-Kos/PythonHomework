

while True:
    number = int(input())
    if 0<=number<=100:
        break
    else:
        print('Enter a number between 1 and 100')

if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print(number)
