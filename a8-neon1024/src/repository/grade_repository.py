class GradesRepository:

    def __init__(self):
        self.__all_grades = []

    def get_all_grades(self):
        return self.__all_grades

    def save(self, updated_list):
        self.__all_grades = updated_list
