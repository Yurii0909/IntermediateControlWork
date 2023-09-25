import json
import os
import csv
from note import Note
from collections import OrderedDict
from datetime import datetime

class NoteManager:
    def __init__(self):
        self.notes = []
        self.create_files_if_not_exist()

    def create_files_if_not_exist(self):
        for file in ['notes.json', 'notes.csv']:
            if not os.path.isfile(file):
                with open(file, 'w'): pass

    def add_note(self):
        title = input("Введите заголовок: ")
        if not title:
            print("ERROR: Заголовок не может быть пустым.")
            return  
        body = input("Введите заметку: ")
        if not body:
            print("ERROR: Заметка не может быть пустой.")
            return
        note = Note(title, body)
        note.note_id = len(self.notes) + 1
        self.notes.append(note)

        while True:
            print("1 - Сохранить в JSON")
            print("2 - Сохранить в CSV")
            print("0 - Выйти в меню")

            choice = input("Выберите действие: ")
            
            if choice == "1":
                self.save_to_json(note)
                break
            elif choice == "2":
                self.save_to_csv(note)
                break
            elif choice == "0":
                break
            else:
                print("ERROR: Неправильный выбор.")

        print("Заметка сохранена.")

    def save_to_json(self, note):
        note.updated_at = datetime.now()
        data = {"id": note.note_id, "title": note.note_title, "body": note.note_body, "created_at":
note.created_at.strftime('%Y-%m-%d %H:%M:%S'), "updated_at": note.updated_at.strftime('%Y-%m-%d %H%:M:%S')}
        with open('notes.json', 'a') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')

    def save_to_csv(self, note):
        note.updated_at = datetime.now()
        with open('notes.csv', mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow([note.note_title, note.note_body, note.created_at.strftime('%Y-%m-%d %H:%M:%S'), note.updated_at.strftime('%Y-%m-%d %H:%M:%S') if note.updated_at else '-'])

    def read_notes(self):
        notes_ordered_dict = OrderedDict()
        for note in self.notes:
            notes_ordered_dict[note] = None

        while True:
            print("Что вы хотите сделать?")
            print("0 - Выйти в меню")

            i = 1
            for note in notes_ordered_dict:
                print(f"{i} - {note}")
                i += 1

            choice = input("Выберите действие: ")

            if choice == "0":
                break
            elif choice.isdigit() and int(choice) in range(1, i):
                note = list(notes_ordered_dict.keys())[int(choice) - 1]
                print(note.note_body)
                while True:
                    print("1 - Редактировать")
                    print("2 - Прочитать")
                    print("0 - Выйти в меню")

                    ch = input("Выберите действие: ")
                    if ch == "1":
                        new_body = input("Введите новую заметку: ")
                        self.edit_note_body(note, new_body)
                        print("Заметка обновлена.")
                    elif ch == "2":
                        print("Заметка:")
                        print(note.note_body)
                    elif ch == "0":
                        break
                    else:
                        print("ERROR: Неправильный выбор.")
            else:
                print("ERROR: Неправильный выбор.")

    def edit_note_body(self, note, new_body):
        note.note_body = new_body
        note.updated_at = datetime.now()

    def load_from_json(self):
        with open('notes.json') as f:
            for line in f:
                data = json.loads(line)
                note = Note(data["title"], data["body"])
                note.note_id = data["id"]
                note.created_at = datetime.strptime(data["created_at"], '%Y-%m-%d %H:%M:%S')
                note.updated_at = datetime.strptime(data["updated_at"], '%Y-%m-%d %H:%M:%S') if data["updated_at"] != '-' else None
                self.notes.append(note)

    def load_from_csv(self):
        with open('notes.csv', mode='r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                note = Note(row[0], row[1])
                note.note_id = len(self.notes) + 1
                note.created_at = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                note.updated_at = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S') if row[3] != '-' else None
                self.notes.append(note)
