while True:
    num1 = int(input("Enter number or -1 to stop:"))
    if num1 != -1: 
        num2 = int(input("Enter degree:"))
        print(num1 ** num2)
    else:
        break
