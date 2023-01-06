import random

from src.domain.discipline import Discipline
from src.domain.custom_exceptions import IdAlreadyExistsError, IdDoesNotExistsError, NameDoesNotExistsError
from src.validator.discipline_service_validator import DisciplinesServiceValidator


class DisciplinesService:

    def __init__(self, disciplines_repository):
        self.__disciplines_repository = disciplines_repository
        self.__disciplines_service_validator = DisciplinesServiceValidator()

        random_generated_disciplines = self.__get_random_generated_disciplines(0)

        self.__undo_list = [random_generated_disciplines]
        self.__disciplines_repository.save(random_generated_disciplines)

    @staticmethod
    def __get_random_generated_disciplines(number_of_random_disciplines_to_generate):
        random_generated_disciplines = []

        discipline_names = ["Mathematics", "Computer Science", "Computational Logic", "Fundamentals of Programming", "Computer Systems Architecture", "C Programming"]

        for index in range(number_of_random_disciplines_to_generate):
            discipline_id = random.randint(100, 999)
            discipline_name = discipline_names[index]
            discipline = Discipline(discipline_id, discipline_name)

            random_generated_disciplines.append(discipline)

        return random_generated_disciplines

    def add_discipline(self, discipline_id, discipline_name):
        OLD_LIST = -1   # index of the last list of undo_list

        all_disciplines = list(self.__disciplines_repository.get_all_disciplines())

        if self.__disciplines_service_validator.validate_uniqueness(all_disciplines, discipline_id):

            discipline = Discipline(discipline_id, discipline_name)

            all_disciplines.append(discipline)

            if all_disciplines != self.__undo_list[OLD_LIST]:
                self.__disciplines_repository.save(all_disciplines)
                self.__undo_list.append(all_disciplines)

        else:
            raise IdAlreadyExistsError()

    def remove_discipline(self, removing_id):
        OLD_LIST = -1   # index of the last list of undo_list

        all_disciplines = list(self.__disciplines_repository.get_all_disciplines())

        if self.__disciplines_service_validator.validate_existence(all_disciplines, removing_id):

            index = 0

            while index < len(all_disciplines):
                if all_disciplines[index].get_id() == removing_id:
                    all_disciplines.pop(index)
                else:
                    index += 1

            if all_disciplines != self.__undo_list[OLD_LIST]:
                self.__disciplines_repository.save(all_disciplines)
                self.__undo_list.append(all_disciplines)

        else:
            raise IdDoesNotExistsError()

    def update_discipline(self, updating_id, new_discipline_id, new_discipline_name):
        OLD_LIST = -1  # index of the last list of undo_list

        all_disciplines = list(self.__disciplines_repository.get_all_disciplines())

        if self.__disciplines_service_validator.validate_existence(all_disciplines, updating_id):

            for index in range(0, len(all_disciplines)):
                if all_disciplines[index].get_id() == updating_id:
                    all_disciplines[index].set_id(new_discipline_id)
                    all_disciplines[index].set_name(new_discipline_name)

            if all_disciplines != self.__undo_list[OLD_LIST]:
                self.__disciplines_repository.save(all_disciplines)
                self.__undo_list.append(all_disciplines)

        else:
            raise IdDoesNotExistsError()

    def search_disciplines_by_id(self, searching_id):
        all_disciplines = self.__disciplines_repository.get_all_disciplines()

        target_disciplines = []

        for discipline in all_disciplines:
            if discipline.get_id() == searching_id:
                target_disciplines.append(discipline)

        if not target_disciplines:
            raise IdDoesNotExistsError()

        return target_disciplines

    def search_disciplines_by_name(self, searching_name):
        all_disciplines = self.__disciplines_repository.get_all_disciplines()

        target_disciplines = []

        for discipline in all_disciplines:
            if str(discipline.get_name()).lower() == searching_name:
                target_disciplines.append(discipline)

        if not target_disciplines:
            raise NameDoesNotExistsError()

        return target_disciplines

    def get_all_disciplines(self):
        return self.__disciplines_repository.get_all_disciplines()
