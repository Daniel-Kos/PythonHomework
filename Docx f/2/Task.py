all_products = [
    {
        'name': 'Ноутбук',
        'categories': frozenset(['Электроника', 'Компьютеры', 'Гаджеты'])
    },
    {
        'name': 'Смартфон',
        'categories': frozenset(['Электроника', 'Гаджеты', 'Связь'])
    },
    {
        'name': 'Мышь',
        'categories': frozenset(['Компьютеры', 'Аксессуары'])
    },
    {
        'name': 'Клавиатура',
        'categories': frozenset(['Компьютеры', 'Аксессуары'])
    },
    {
        'name': 'Книга "Python"',
        'categories': frozenset(['Книги', 'Программирование'])
    }
]

# в тз небыло задания сделать нормальное отображение при использование вывода всех продуктов

def find_by_category(category):
    found_products = set()
    for product in all_products:
        if category in product['categories']:
            found_products.add(product['name'])
    return found_products

def add_product_dict(add_list_category, add_product_name):
    add_products = {
        'name': add_product_name,
        'categories': frozenset(add_list_category)
    }
    all_products.append(add_products)

while True:
    print("1. Добавить продукт\n2. Показать все продукты\n3. Найти продукты по категории\n4. Выход")

    try:
        number_category = int(input("Выберите действие: "))
    except ValueError:
        print("Пожалуйста, введите число от 1 до 4.")
        continue

    if number_category == 1:
        add_product_name = str(input("Введите название продукта: "))
        add_list_category = []
        print("Введите категории (для завершения введите -1):")

        while True:
            add_category_name = input()
            if add_category_name == "-1":
                break
            add_list_category.append(add_category_name)
        add_product_dict(add_list_category, add_product_name)
        print(f"Продукт '{add_product_name}' добавлен.")

    elif number_category == 2:
        print(all_products)

    elif number_category == 3:
        category_to_find = input("Введите категорию для поиска: ")
        found = find_by_category(category_to_find)
        if found:
            print(f"Найдено в категории '{category_to_find}': {found}")
        else:
            print("Ничего не найдено.")

    elif number_category == 4:
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод, введите число от 1 до 4.")
