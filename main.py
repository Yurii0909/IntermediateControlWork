from note import Note
from note_manager import NoteManager

def main():
    note_manager = NoteManager()

    while True:
        print("Выберите действие:")
        print("1 - Создать заметку")
        print("2 - Читать заметки")
        print("3 - Загрузить заметки из файла JSON")
        print("4 - Загрузить заметки из файла CSV")
        print("0 - Выход")
        
        choice = input("Выберите пункт меню: ")

        if choice == "1":
            note_manager.add_note()
        elif choice == "2":
            note_manager.read_notes()
        elif choice == "3":
            note_manager.load_from_json()
            print("Заметки загружены из JSON файла.")
        elif choice == "4":
            note_manager.load_from_csv()
            print("Заметки загружены из CSV файла.")
        elif choice == "0":
            break
        else:
            print("ERROR: Неправильный выбор. Пожалуйста, выберите один из предложенных вариантов.")

if __name__ == "__main__":
    main()
