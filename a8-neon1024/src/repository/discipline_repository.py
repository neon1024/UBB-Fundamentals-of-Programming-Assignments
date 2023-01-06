class DisciplinesRepository:

    def __init__(self):
        self.__all_disciplines = []

    def get_all_disciplines(self):
        return self.__all_disciplines

    def save(self, updated_list):
        self.__all_disciplines = updated_list
