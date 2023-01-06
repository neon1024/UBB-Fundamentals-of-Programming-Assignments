class Student:

    def __init__(self, student_id: int, student_name: str, student_group: int):

        self.__student_id = student_id
        self.__student_name = student_name
        self.__student_group = student_group

    # TODO: use @property
    def get_id(self):

        return self.__student_id

    def set_id(self, new_id: int):

        self.__student_id = new_id

    def get_name(self):

        return self.__student_name

    def set_name(self, new_name: str):

        self.__student_name = new_name

    def get_group(self):

        return self.__student_group

    def set_group(self, new_group):

        self.__student_group = new_group

    def __repr__(self):

        return str(self)

    def __str__(self):

        return f"Id: {self.__student_id}, Name: {self.__student_name}, Group: {self.__student_group}"
