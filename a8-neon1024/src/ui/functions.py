# TODO: correct input
from src.domain.custom_exceptions import InvalidInputError


def contains_digits(string):
    return any(string.isdigit() for character in string)


def get_discipline_id_from_console():
    while True:
        try:

            discipline_id = int(input("Discipline Id: "))

            return discipline_id

        except Exception as error:
            print(str(error))


def get_discipline_name_from_console():
    while True:
        try:

            discipline_name = input("Discipline Name: ")

            if contains_digits(discipline_name):
                raise InvalidInputError()

            return discipline_name

        except InvalidInputError as iie:
            print(str(iie))


def get_student_id_from_console():
    while True:
        try:

            student_id = int(input("Student Id: "))

            return student_id

        except Exception as error:
            print(str(error))


def get_student_name_from_console():
    while True:
        try:

            student_name = input("Student Name: ")

            if contains_digits(student_name):
                raise InvalidInputError()

            return student_name

        except InvalidInputError as iie:
            print(str(iie))


def get_grade_values(number_of_grades):
    grade_values = []

    for index in range(0, number_of_grades):
        grade_value = float(input(f"Grade {index}:"))
        grade_values.append(grade_value)

    return grade_values
