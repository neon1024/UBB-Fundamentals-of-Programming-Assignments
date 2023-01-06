import random

from src.domain.custom_exceptions import IdAlreadyExistsError, IdDoesNotExistsError, NameDoesNotExistsError
from src.domain.student import Student
from src.validator.student_service_validator import StudentsServiceValidator


class StudentsService:

    def __init__(self, students_repository):
        self.__students_repository = students_repository
        self.__students_service_validator = StudentsServiceValidator()

        random_generated_students = self.__get_random_generated_students(0)

        self.__undo_list = [random_generated_students]
        self.__students_repository.save(random_generated_students)

    @staticmethod
    def __get_random_generated_students(number_of_random_students_to_generate):
        random_generated_students = []

        first_names = ["John", "Alex", "Steve", "Amy", "Andrew", "Jonathan", "David"]
        last_names = ["Adams", "Smith", "Harvey", "Miller", "Williams", "Snow"]

        for index in range(number_of_random_students_to_generate):
            student_id = random.randint(100, 999)
            student_name = random.choice(first_names) + " " + random.choice(last_names)
            student = Student(student_id, student_name)
            random_generated_students.append(student)

        return random_generated_students

    def add_student(self, student_id, student_name):
        OLD_LIST = -1   # index of the last list of undo_list

        all_students = list(self.__students_repository.get_all_students())

        if self.__students_service_validator.validate_uniqueness(all_students, student_id):
            student = Student(student_id, student_name)

            all_students.append(student)

            if all_students != self.__undo_list[OLD_LIST]:
                self.__students_repository.save(all_students)
                self.__undo_list.append(all_students)
        else:
            raise IdAlreadyExistsError()

    def remove_student(self, removing_id):
        OLD_LIST = -1   # index of the last list of undo_list

        all_students = self.__students_repository.get_all_students()

        if self.__students_service_validator.validate_existence(all_students, removing_id):

            index = 0

            while index < len(all_students):
                if all_students[index].get_id() == removing_id:
                    all_students.pop(index)
                else:
                    index += 1

            if all_students != self.__undo_list[OLD_LIST]:
                self.__students_repository.save(all_students)
                self.__undo_list.append(all_students)
        else:
            raise IdDoesNotExistsError()

    def update_student(self, updating_id, new_student_id, new_student_name):
        OLD_LIST = -1   # index of the last list of undo_list

        all_students = list(self.__students_repository.get_all_students())

        if self.__students_service_validator.validate_existence(all_students, updating_id):

            index = 0

            while index < len(all_students):
                if all_students[index].get_id() == updating_id:
                    all_students[index].set_id(new_student_id)
                    all_students[index].set_name(new_student_name)

                index += 1

            if all_students != self.__undo_list[OLD_LIST]:
                self.__students_repository.save(all_students)
                self.__undo_list.append(all_students)

        else:
            raise IdDoesNotExistsError()

    def search_students_by_id(self, searching_id):
        all_students = list(self.__students_repository.get_all_students())

        if self.__students_service_validator.validate_existence(all_students, searching_id):

            target_students = []

            for student in all_students:
                if student.get_id() == searching_id:
                    target_students.append(student)

            return target_students

        else:
            raise IdDoesNotExistsError()

    def search_students_by_name(self, searching_name):
        all_students = list(self.__students_repository.get_all_students())

        target_students = []

        for student in all_students:
            if str(student.get_name()).lower() == searching_name:
                target_students.append(student)

        if not target_students:
            raise NameDoesNotExistsError()

        return target_students

    def get_all_students(self):
        return self.__students_repository.get_all_students()
