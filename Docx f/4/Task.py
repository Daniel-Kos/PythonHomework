def call_counter(func):
    """
    Декоратор, который подсчитывает количество вызовов функции
    и выводит имя функции, аргументы и порядковый номер вызова.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Функция {func.__name__} вызвана {wrapper.count} раз")
        print(f"Аргументы: {args}")
        if kwargs:
            print(f"Именованные аргументы: {kwargs}")
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


@call_counter
def add(a, b):
    """Возвращает сумму двух чисел."""
    return a + b


@call_counter
def repeat(text, n):
    """Возвращает строку, повторённую n раз."""
    return text * n


if __name__ == "__main__":
    print(add(2, 3))
    print(add(10, 5))
    print(repeat("Hi", 3))

    print(repeat("Hello", 2))
