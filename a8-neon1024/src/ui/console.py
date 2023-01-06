import random

from src.domain.custom_exceptions import IdDoesNotExistsError
from src.ui.functions import get_student_id_from_console, get_student_name_from_console, get_discipline_id_from_console, get_discipline_name_from_console, get_grade_values


class Console:

    def __init__(self, students_service, disciplines_service, grades_service):

        self.__students_service = students_service
        self.__discipline_service = disciplines_service
        self.__grades_service = grades_service

        self.__console_options = {
            "1": self.__manage_students_menu,
            "2": self.__manage_disciplines_menu,
            "3": self.__manage_statistics_menu
        }

        self.__students_options = {
            "1": self.__add_student,
            "2": self.__remove_student,
            "3": self.__update_student,
            "4": self.__list_students,
            "5": self.__grade_student,
            "6": self.__search_students_by_id,
            "7": self.__search_students_by_name
        }

        self.__disciplines_options = {
            "1": self.__add_discipline,
            "2": self.__remove_discipline,
            "3": self.__update_discipline,
            "4": self.__list_disciplines,
            "5": self.__search_disciplines_by_id,
            "6": self.__search_disciplines_by_name
        }

        self.__statistics_options = {
            "1": self.__list_all_grades,
            "2": self.__print_all_students_failing_at_one_or_more_disciplines,
            "3": self.__print_students_with_the_best_school_situation_sorted_in_descending_order_of_their_aggregated_average,
            "4": self.__print_all_disciplines_at_which_there_is_at_least_one_grade_sorted_in_descending_order_of_the_average_grades_received_by_students
        }

    # STUDENTS METHODS
    def __add_student(self):
        student_id = get_student_id_from_console()
        student_name = get_student_name_from_console()

        self.__students_service.add_student(student_id, student_name)

    def __remove_student(self):
        removing_id = get_student_id_from_console()

        self.__students_service.remove_student(removing_id)

        try:
            self.__grades_service.remove_student(removing_id)
        except IdDoesNotExistsError:
            pass

    def __update_student(self):
        updating_id = get_student_id_from_console()
        new_student_id = get_student_id_from_console()
        new_student_name = get_student_name_from_console()

        self.__students_service.update_student(updating_id, new_student_id, new_student_name)

        try:
            self.__grades_service.update_student(updating_id, new_student_id)
        except IdDoesNotExistsError:
            pass

    def __list_students(self):
        all_students = self.__students_service.get_all_students()

        for student in all_students:
            print(student)

    def __grade_student(self):
        discipline_id = get_discipline_id_from_console()
        student_id = get_student_id_from_console()
        number_of_grade_values = int(input("Number of grades: "))

        grade_values = get_grade_values(number_of_grade_values)

        self.__grades_service.grade_student(discipline_id, student_id, grade_values)

    def __search_students_by_id(self):
        searching_id = get_student_id_from_console()

        target_students = list(self.__students_service.search_students_by_id(searching_id))

        for student in target_students:
            print(student)

    def __search_students_by_name(self):
        searching_name = get_student_name_from_console()

        target_students = list(self.__students_service.search_students_by_name(searching_name.lower()))

        for student in target_students:
            print(student)

    # DISCIPLINES METHODS
    def __add_discipline(self):
        discipline_id = get_discipline_id_from_console()
        discipline_name = get_discipline_name_from_console()

        self.__discipline_service.add_discipline(discipline_id, discipline_name)

    def __remove_discipline(self):
        removing_id = get_discipline_id_from_console()

        self.__discipline_service.remove_discipline(removing_id)

        try:
            self.__grades_service.remove_discipline(removing_id)
        except IdDoesNotExistsError:
            pass

    def __update_discipline(self):
        updating_id = get_discipline_id_from_console()
        new_discipline_id = get_discipline_id_from_console()
        new_discipline_name = get_discipline_name_from_console()

        self.__discipline_service.update_discipline(updating_id, new_discipline_id, new_discipline_name)

        try:
            self.__grades_service.update_discipline(updating_id, new_discipline_id)
        except IdDoesNotExistsError:
            pass

    def __list_disciplines(self):
        all_disciplines = self.__discipline_service.get_all_disciplines()

        for discipline in all_disciplines:
            print(discipline)

    def __search_disciplines_by_id(self):
        searching_id = get_discipline_id_from_console()

        target_disciplines = list(self.__discipline_service.search_disciplines_by_id(searching_id))

        for discipline in target_disciplines:
            print(discipline)

    def __search_disciplines_by_name(self):
        searching_name = get_discipline_name_from_console()

        target_disciplines = list(self.__discipline_service.search_disciplines_by_name(searching_name.lower()))

        for discipline in target_disciplines:
            print(discipline)

    # STATISTICS METHODS
    def __generate_random_grades(self, all_students, all_disciplines, number_of_random_grades_to_generate):
        for i in range(number_of_random_grades_to_generate):
            random_discipline = random.choice(all_disciplines)
            random_student = random.choice(all_students)
            discipline_id = random_discipline.get_id()
            student_id = random_student.get_id()
            number_of_grades = random.randint(1, 1)
            grade_values = []

            for j in range(number_of_grades):
                random_grade = random.randint(1, 10)
                grade_values.append(random_grade)

            self.__grades_service.grade_student(discipline_id, student_id, grade_values)

    def __list_all_grades(self):
        all_grades = list(self.__grades_service.get_all_grades())

        for grade in all_grades:
            print(grade)

    def __print_all_students_failing_at_one_or_more_disciplines(self):
        all_students = self.__students_service.get_all_students()
        all_disciplines = self.__discipline_service.get_all_disciplines()

        failing_students = list(self.__grades_service.get_failing_students(all_students, all_disciplines))

        for failing_student in failing_students:
            print(failing_student)

    def __print_students_with_the_best_school_situation_sorted_in_descending_order_of_their_aggregated_average(self):
        all_students = self.__students_service.get_all_students()
        all_disciplines = self.__discipline_service.get_all_disciplines()

        students_aggregated_averages = list(self.__grades_service.get_best_students_in_descending_order(all_students, all_disciplines))

        for student in students_aggregated_averages:
            print("Id:", student["Student Id"], "Name:", student["Student Name"])

    def __print_all_disciplines_at_which_there_is_at_least_one_grade_sorted_in_descending_order_of_the_average_grades_received_by_students(self):
        all_disciplines = self.__discipline_service.get_all_disciplines()
        all_students = self.__students_service.get_all_students()

        disciplines_with_at_least_one_grade = list(self.__grades_service.get_all_disciplines_with_at_least_one_grade_in_descending_order(all_disciplines, all_students))

        for discipline in disciplines_with_at_least_one_grade:
            print("Discipline Id:", discipline["Discipline Id"])

    # CONSOLE MENU
    @staticmethod
    def __print_console_options():
        print("1: Manage students")
        print("2: Manage disciplines")
        print("3: Statistics")

    def run_console(self):
        all_students = self.__students_service.get_all_students()
        all_disciplines = self.__discipline_service.get_all_disciplines()

        self.__generate_random_grades(all_students, all_disciplines, 0)

        while True:
            try:

                self.__print_console_options()

                chosen_option = input("> ")

                self.__console_options[chosen_option]()

            except Exception as error:
                print(str(error))

    # STUDENTS MENU
    @staticmethod
    def __print_students_options():
        print("1: Add student.")
        print("2: Remove student.")
        print("3: Update student.")
        print("4: List students.")
        print("5: Grade student.")
        print("6: Search for students based on ID")
        print("7: Search for students based on name")

    def __manage_students_menu(self):
        while True:
            try:

                print("0: BACK")
                self.__print_students_options()

                chosen_option = input("> ")

                if chosen_option == "0":
                    break
                else:
                    self.__students_options[chosen_option]()

            except Exception as error:
                print(str(error))

    # DISCIPLINES MENU
    @staticmethod
    def __print_disciplines_options():
        print("1: Add discipline.")
        print("2: Remove discipline.")
        print("3: Update discipline.")
        print("4: List disciplines.")
        print("5: Search for disciplines based on ID")
        print("6: Search for disciplines based on name")

    def __manage_disciplines_menu(self):
        while True:
            try:

                print("0: BACK")
                self.__print_disciplines_options()

                chosen_option = input("> ")

                if chosen_option == "0":
                    break
                else:
                    self.__disciplines_options[chosen_option]()

            except Exception as error:
                print(str(error))

    # STATISTICS MENU
    @staticmethod
    def __print_statistics_options():
        print("1: List all grades.")
        print("2: Show all students failing at one or more discipline.")
        print("3: Show students with the best school situation, sorted in descending order of their aggregated average.")
        print("4: Show all disciplines at which there is at least one grade, sorted in descending order of the average grade(s) received by all students.")

    def __manage_statistics_menu(self):
        while True:
            try:

                print("0: BACK")
                self.__print_statistics_options()

                chosen_option = input("> ")

                if chosen_option == "0":
                    break
                else:
                    self.__statistics_options[chosen_option]()

            except Exception as error:
                print(str(error))
