class Discipline:

    def __init__(self, discipline_id: int, discipline_name: str):
        self.__discipline_id = discipline_id
        self.__discipline_name = discipline_name

    def get_id(self):
        return self.__discipline_id

    def set_id(self, new_discipline_id: int):
        self.__discipline_id = new_discipline_id

    def get_name(self):
        return self.__discipline_name

    def set_name(self, new_discipline_name: str):
        self.__discipline_name = new_discipline_name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Id: {self.__discipline_id}, Name: {self.__discipline_name}"
