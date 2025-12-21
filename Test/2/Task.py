class Character:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        print("Персонаж атакует!")
    
    def __str__(self):
        return f"Имя: {self.name}, Здоровье: {self.health}, Сила: {self.strength}"


class Warrior(Character):
    def __init__(self, name, health, strength):
        # Увеличиваем здоровье и силу для воина
        super().__init__(name, health + 30, strength + 10)
    
    def attack(self):
        print("Воин наносит мощный удар мечом!")


class Mage(Character):
    def __init__(self, name, health, strength, mana):
        # Уменьшаем силу для мага
        super().__init__(name, health, strength - 5)
        self.mana = mana
    
    def attack(self):
        print("Маг выпускает огненный шар!")
    
    def __str__(self):
        return f"{super().__str__()}, Мана: {self.mana}"


def create_character():
    print("\nСоздание персонажа")
    print("1. Воин")
    print("2. Маг")
    
    choice = input("Выберите тип персонажа (1 или 2): ")
    
    name = input("Введите имя персонажа: ")
    
    try:
        if choice == "1":
            health = int(input("Введите здоровье: "))
            strength = int(input("Введите силу: "))
            character = Warrior(name, health, strength)
            print(f"Создан воин: {character}")
            return character
        
        elif choice == "2":
            health = int(input("Введите здоровье: "))
            strength = int(input("Введите силу: "))
            mana = int(input("Введите количество маны: "))
            character = Mage(name, health, strength, mana)
            print(f"Создан маг: {character}")
            return character
        
        else:
            print("Некорректный выбор!")
            return None
    except ValueError:
        print("Ошибка! Введите числовые значения.")
        return None


def main():
    characters = []
    
    # Создаем персонажей из условия
    w = Warrior("Арагорн", 120, 20)
    m = Mage("Гендальф", 80, 10, 200)
    characters.extend([w, m])
    
    print("Добро пожаловать в систему персонажей!")
    
    while True:
        print("\n" + "="*40)
        print("МИНИ-МЕНЮ:")
        print("1. Создать персонажа")
        print("2. Показать всех персонажей")
        print("3. Атака персонажа")
        print("4. Выход")
        
        choice = input("Выберите пункт меню (1-4): ")
        
        if choice == "1":
            new_char = create_character()
            if new_char:
                characters.append(new_char)
        
        elif choice == "2":
            print("\nСписок всех персонажей:")
            print("="*40)
            if not characters:
                print("Персонажей пока нет!")
            else:
                for i, char in enumerate(characters, 1):
                    print(f"{i}. {char}")
        
        elif choice == "3":
            if not characters:
                print("Нет персонажей для атаки!")
                continue
            
            print("\nВыберите персонажа для атаки:")
            for i, char in enumerate(characters, 1):
                print(f"{i}. {char.name}")
            
            try:
                char_num = int(input("Введите номер персонажа: ")) - 1
                if 0 <= char_num < len(characters):
                    characters[char_num].attack()
                else:
                    print("Неверный номер персонажа!")
            except ValueError:
                print("Ошибка! Введите число.")
        
        elif choice == "4":
            print("Выход из программы...")
            break
        
        else:
            print("Некорректный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()