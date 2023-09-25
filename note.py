from datetime import datetime

class Note:
    def __init__(self, title, body):
        self.__note_id = None
        self.__note_title = title
        self.__note_body = body
        self.__created_at = datetime.now()
        self.__updated_at = None

    @property
    def note_id(self):
        return self.__note_id

    @note_id.setter
    def note_id(self, value):
        self.__note_id = value

    @property
    def note_title(self):
        return self.__note_title

    @note_title.setter
    def note_title(self, value):
        self.__note_title = value

    @property
    def note_body(self):
        return self.__note_body

    @note_body.setter
    def note_body(self, value):
        self.__note_body = value

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, value):
        self.__updated_at = value

    def __repr__(self):
        return f"{self.note_id} - {self.note_title} ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')}) ({self.updated_at.strftime('%Y-%m-%d %H:%M:%S') if self.updated_at else '-'})"
