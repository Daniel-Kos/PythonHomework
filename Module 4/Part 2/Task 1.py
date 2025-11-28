number1 = float(input("Enter first number:"))
number2 = float(input("Enter second number:"))
action = str(input("Enter action (-,+,*,/):"))


if action == "+":
    result = number1 + number2

elif action == "-":
    result = number1 - number2

elif action == "*":
    result = number1 * number2

elif action == "/":
    result = number1 / number2

print(result)