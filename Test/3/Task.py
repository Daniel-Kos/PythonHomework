def load_notes():
    """Загружает заметки из файла и возвращает список кортежей"""
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = []
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(" | ", 1)
                    if len(parts) == 2:
                        notes.append((parts[0], parts[1]))
            return notes
    except FileNotFoundError:
        return []

def save_notes(notes):
    """Сохраняет все заметки в файл"""
    with open("notes.txt", "w", encoding="utf-8") as file:
        for category, text in notes:
            file.write(f"{category} | {text}\n")

def add_note():
    """Добавляет новую заметку"""
    category = input("Введите категорию: ").strip()
    text = input("Введите текст заметки: ").strip()
    
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(f"{category} | {text}\n")
    print("Заметка добавлена!\n")

def find_by_category(category):
    """Находит заметки по категории"""
    notes = load_notes()
    results = [note for note in notes if note[0].lower() == category.lower()]
    
    if results:
        print(f"\nНайдено заметок в категории '{category}': {len(results)}")
        for cat, text in results:
            print(f"- {text} ({cat})")
    else:
        print(f"Заметок в категории '{category}' не найдено")
    print()

def search_word(word):
    """Ищет заметки по ключевому слову"""
    notes = load_notes()
    word_lower = word.lower()
    results = []
    
    for category, text in notes:
        if word_lower in category.lower() or word_lower in text.lower():
            results.append((category, text))
    
    if results:
        print(f"\nНайдено заметок со словом '{word}': {len(results)}")
        for cat, text in results:
            print(f"- {text} ({cat})")
    else:
        print(f"Заметок со словом '{word}' не найдено")
    print()

def show_all_notes():
    """Показывает все заметки"""
    notes = load_notes()
    
    if not notes:
        print("Заметок пока нет\n")
        return
    
    print(f"\nВсе заметки ({len(notes)}):")
    for i, (category, text) in enumerate(notes, 1):
        print(f"{i}. {text} ({category})")
    print()

def main():
    """Основное меню программы"""
    while True:
        print("=" * 30)
        print("МЕНЕДЖЕР ЗАМЕТОК")
        print("=" * 30)
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Найти по категории")
        print("4. Поиск по слову")
        print("5. Выход")
        
        choice = input("\nВыберите действие (1-5): ").strip()
        
        if choice == "1":
            add_note()
        elif choice == "2":
            show_all_notes()
        elif choice == "3":
            category = input("Введите категорию для поиска: ").strip()
            find_by_category(category)
        elif choice == "4":
            word = input("Введите слово для поиска: ").strip()
            search_word(word)
        elif choice == "5":
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.\n")

if __name__ == "__main__":
    # Создаем файл, если он не существует
    try:
        open("notes.txt", "a", encoding="utf-8").close()
    except:
        pass
    
    main()