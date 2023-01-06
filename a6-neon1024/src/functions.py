"""

@author: neon1024

"""


#
# The program's functions are implemented here. There is no user interaction in this file, therefore no input/print
# statements. Functions here communicate via function parameters, the return statement and raising of exceptions.
#


import random
from math import sqrt


def print_complex_number(complex_number: dict):

    real_part = complex_number["real_part"]
    imaginary_part = complex_number["imaginary_part"]

    if real_part == 0:
        print(str(imaginary_part) + "i")
        return

    if imaginary_part == 0:
        print(real_part)
        return

    if real_part == 0 and imaginary_part == 0:
        print(0)
        return

    in_between_sign = "+" if "+" and "-" not in str(imaginary_part) else ""

    print(str(real_part) + in_between_sign + str(imaginary_part) + "i")


def get_a_random_complex_random():

    return {"real_part": random.randint(-100, 100), "imaginary_part": random.randint(-100, 100)}


def get_a_list_of_random_complex_numbers():

    list_of_random_complex_numbers = []

    for index in range(0, 10):
        list_of_random_complex_numbers.append(get_a_random_complex_random())

    return list_of_random_complex_numbers


def get_complex_number(complex_number_string: str):

    complex_number_string = complex_number_string.replace("i", "j")
    real_part = complex(complex_number_string).real

    if real_part == int(real_part):
        real_part = int(real_part)

    imaginary_part = complex(complex_number_string).imag

    if imaginary_part == int(imaginary_part):
        imaginary_part = int(imaginary_part)

    return {"real_part": real_part, "imaginary_part": imaginary_part}


def get_position(position_string: str):

    return int(position_string)


def get_complex_number_modulo(complex_number: dict):

    real_part = complex_number["real_part"]
    imaginary_part = complex_number["imaginary_part"]

    return sqrt(real_part**2 + imaginary_part**2)


# option E instructions
def undo_the_last_operation_on_the_list(list_of_lists_of_complex_numbers: list):

    list_of_lists_of_complex_numbers.pop()


# option D instructions
def keep_in_the_list_only_the_complex_numbers_with_a_specific_modulo_property(list_of_complex_numbers: list,
                                                                              symbol: str, number):

    new_list_of_complex_numbers = []

    for index in range(0, len(list_of_complex_numbers)):
        complex_number = list_of_complex_numbers[index]
        complex_number_modulo = get_complex_number_modulo(complex_number)

        if symbol == "=":
            if complex_number_modulo == number:
                new_list_of_complex_numbers.append(complex_number)

        elif symbol == "<":
            if complex_number_modulo < number:
                new_list_of_complex_numbers.append(complex_number)

        elif symbol == ">":
            if complex_number_modulo > number:
                new_list_of_complex_numbers.append(complex_number)

    list_of_complex_numbers.clear()
    list_of_complex_numbers.extend(new_list_of_complex_numbers)


def keep_in_the_list_only_the_complex_numbers_with_imaginary_part_zero(list_of_complex_numbers: list):

    list_of_complex_numbers_having_imaginary_part_zero = []

    for index in range(0, len(list_of_complex_numbers)):
        complex_number = list_of_complex_numbers[index]

        if complex_number["imaginary_part"] == 0:
            list_of_complex_numbers_having_imaginary_part_zero.append(complex_number)

    list_of_complex_numbers.clear()

    list_of_complex_numbers.extend(list_of_complex_numbers_having_imaginary_part_zero)


# option C instructions
def print_complex_numbers_from_list_of_complex_numbers_by_modulo_expression(list_of_complex_numbers: list, symbol: str,
                                                                            number: float):

    for index in range(0, len(list_of_complex_numbers)):

        complex_number = list_of_complex_numbers[index]

        complex_number_modulo = get_complex_number_modulo(complex_number)

        if symbol == "<":

            if complex_number_modulo < number:

                print_complex_number(complex_number)

        elif symbol == "=":

            if complex_number_modulo == number:

                print_complex_number(complex_number)

        elif symbol == ">":

            if complex_number_modulo > number:

                print_complex_number(complex_number)


def print_real_numbers_from_list_of_complex_numbers_between_two_indexes(
        list_of_complex_numbers: list, start_position: int, end_position: int):

    for index in range(start_position, end_position + 1):

        if list_of_complex_numbers[index]["imaginary_part"] == 0:

            print(list_of_complex_numbers[index]["real_part"])


def print_list_of_complex_numbers(list_of_complex_numbers: list):

    print("\nList of complex numbers:\n")

    for complex_number in list_of_complex_numbers:

        print_complex_number(complex_number)


# option B instructions
def test_remove_a_complex_number_from_the_list(list_of_complex_numbers: list, position: int):

    test_list = list_of_complex_numbers[:]

    remove_a_complex_number_from_the_list(test_list, 0)

    assert test_list != list_of_complex_numbers


def remove_a_complex_number_from_the_list(list_of_complex_numbers: list, position: int):

    left_list = list_of_complex_numbers[:position]

    right_list = list_of_complex_numbers[position + 1:]

    list_of_complex_numbers.clear()

    list_of_complex_numbers.extend(left_list + right_list)


def test_remove_complex_numbers_from_the_list_between_two_indexes(list_of_complex_numbers: list, start_position: int, end_position: int):

    test_list = list_of_complex_numbers[:]

    remove_complex_numbers_from_the_list_between_two_indexes(test_list, 0, len(test_list) - 1)

    assert test_list != list_of_complex_numbers


def remove_complex_numbers_from_the_list_between_two_indexes(list_of_complex_numbers: list, start_position: int, end_position: int):

    left_list = list_of_complex_numbers[:start_position]

    right_list = list_of_complex_numbers[end_position + 1:]

    list_of_complex_numbers.clear()

    list_of_complex_numbers.extend(left_list + right_list)


def test_replace_a_complex_number_with_a_new_one(list_of_complex_numbers: list, old_number: dict, new_number: dict):

    test_list = list_of_complex_numbers[:]

    changed = False

    for index in range(0, len(test_list)):
        if test_list[index] == old_number:
            test_list[index] = new_number
            changed = True

    if changed:
        assert test_list != list_of_complex_numbers


def replace_a_complex_number_with_a_new_one(list_of_complex_numbers: list, old_number: dict, new_number: dict):

    for index in range(0, len(list_of_complex_numbers)):

        if list_of_complex_numbers[index] == old_number:

            list_of_complex_numbers[index] = new_number


# option A instructions
def test_insert_a_complex_number_to_the_list(list_of_complex_numbers: list, complex_number: dict, position: int):

    test_list = list_of_complex_numbers[:]

    insert_a_complex_number_to_the_list(test_list, {"real_part": 1, "imaginary_part": 1}, 0)

    assert test_list[0] == {"real_part": 1, "imaginary_part": 1}

    insert_a_complex_number_to_the_list(test_list, {"real_part": 1, "imaginary_part": 1}, 1)

    assert test_list[1] == {"real_part": 1, "imaginary_part": 1}


def insert_a_complex_number_to_the_list(list_of_complex_numbers: list, complex_number: dict, position: int):

    if len(list_of_complex_numbers) == 0 and position == 0:

        list_of_complex_numbers.append(complex_number)

        return

    if abs(len(list_of_complex_numbers) - position) == 0:

        list_of_complex_numbers.append(complex_number)

        return

    list_of_complex_numbers[position] = complex_number


def test_add_a_complex_number_to_the_list(list_of_complex_numbers: list, complex_number: dict):

    test_list = list_of_complex_numbers[:]

    add_a_complex_number_to_the_list(test_list, {"real_part": 1, "imaginary_part": 1})

    assert test_list[-1] == {"real_part": 1, "imaginary_part": 1}


def add_a_complex_number_to_the_list(list_of_complex_numbers: list, complex_number: dict):

    list_of_complex_numbers.append(complex_number)
