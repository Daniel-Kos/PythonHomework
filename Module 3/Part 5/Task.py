def print_right_upper_triangle(height):
    for i in range(height):
        print(' ' * i + '*' * (height - i))
 
def print_left_lower_triangle2(height):
    for i in range(height):
        print('*' * (i + 1) + ' ' * (height + i))
 
def print_triangle_upside_down(height):
    for i in range(height // 2):
        print(' ' * i + '*' * (2 * (height // 2 - i) - 1))
 
def print_triangle(height):
    for i in range(height // 2):
        print(' ' * (height // 2 - i - 1) + '*' * (2 * i + 1))
 
def print_triangles_simultaneously(height):
    print_triangle_upside_down(height)
    print_triangle(height)
 
def print_left_lower_triangle9(height):
    for i in range(height):
        print('*' * (height - i) + ' ' * (i - 1))
 
def print_left_lower_triangle10(height):
    for i in range(height):
        print(' ' * (height - i - 1) + '*' * (i + 1))
 
def print_left_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

    for i in range(height - 1, 0, -1):
        print('*' * i)

def print_right_triangle(height):
    for i in range(1, height + 1):
        spaces = ' ' * (height - i)
        stars = '*' * i
        print(spaces + stars)

    for i in range(height - 1, 0, -1):
        spaces = ' ' * (height - i)
        stars = '*' * i
        print(spaces + stars)

def print_right_left_triangle(height):
    for i in range(height):
        stars = 2 * i + 1
    print("*" * stars)

while True:
    print("\nМеню:")
    print("1. Треугольник в правом верхнем углу")
    print("2. Треугольник в левом нижнем углу")
    print("3. Равносторонний треугольник с основанием по верхнему краю")
    print("4. Равносторонний треугольник с основанием по нижнему краю")
    print("5. Равносторонние треугольники с основаниями по верхнему и нижнему краям")
    print("6. Треугольник в верхнем левом углу")
    print("7. Треугольник в нижнем правом углу")
    print("8. Треугольник с основанием слево")
    print("9. Треугольник с основанием справо")
    print("0. Выход")
 
    choice = int(input("Введите свой выбор: "))
 
    if choice == 1:
        height = int(input("Введите размер квадрата: "))
        print_right_upper_triangle(height)
    elif choice == 2:
        height = int(input("Введите размер квадрата: "))
        print_left_lower_triangle2(height)
    elif choice == 3:
        height = int(input("Введите размер квадрата: "))
        print_triangle_upside_down(height)
    elif choice == 4:
        height = int(input("Введите размер квадрата: "))
        print_triangle(height)
    elif choice == 5:
        height = int(input("Введите размер квадрата: "))
        print_triangles_simultaneously(height)
    elif choice == 6:
        height = int(input("Введите размер квадрата: "))
        print_left_lower_triangle9(height)
    elif choice == 7:
        height = int(input("Введите размер квадрата: "))
        print_left_lower_triangle10(height)
    elif choice == 8:
        height = int(input("Введите размер квадрата:"))
        print_left_triangle(height)
    elif choice == 9:
        height = int(input("Введите размер квадрата:"))
        print_right_triangle(height)
    elif choice == 10:
        height = int(input("Введите размер квадрата:"))
        print_right_left_triangle(height)
    elif choice == 0:
        break
