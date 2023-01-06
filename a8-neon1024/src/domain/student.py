class Student:

    def __init__(self, student_id: int, student_name: str):
        self.__student_id = student_id
        self.__student_name = student_name

    def get_id(self):
        return self.__student_id

    def set_id(self, new_student_id: int):
        self.__student_id = new_student_id

    def get_name(self):
        return self.__student_name

    def set_name(self, new_student_name: str):
        self.__student_name = new_student_name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Id: {self.__student_id}, Name: {self.__student_name}"
