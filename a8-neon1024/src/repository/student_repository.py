class StudentsRepository:

    def __init__(self):
        self.__all_students = []

    def get_all_students(self):
        return self.__all_students

    def save(self, updated_list):
        self.__all_students = updated_list
