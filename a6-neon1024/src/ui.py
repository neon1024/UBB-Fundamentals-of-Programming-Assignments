"""

@author: neon1024

"""


#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements)
# are found here
#


from functions import *


# prints
def print_option_A_add_a_number_instructions():

    print("\nadd <number>")
    print("\ninsert <number> at <position>")


def print_option_B_modify_numbers_instructions():

    print("\nremove <position>")
    print("\nremove <start position> to <end position>")
    print("\nreplace <old number> with <new number>")


def print_option_C_display_numbers_having_different_properties_instructions():

    print("\nlist")
    print("\nlist real <start position> to <end position>")
    print("\nlist modulo [ < | = | > ] <number>")


def print_option_D_filter_the_list_instructions():

    print("\nfilter real")
    print("\nfilter modulo [ < | = | > ] <number>")


def print_option_E_undo_instructions():

    print("\nundo")


# options
def option_A_add_a_number():

    print_option_A_add_a_number_instructions()

    user_input = input("\n>")
    user_input = user_input.strip()
    user_input_elements = user_input.split(" ")
    instruction = user_input_elements[0]

    try:
        complex_number = get_complex_number(user_input_elements[1])

    except ValueError as ve:
        print("\nInvalid complex number representation:", ve)

        return

    except IndexError as ie:
        print("\nInvalid instruction syntax:", ie)

        return

    if len(user_input_elements) == 4:
        try:
            position = get_position(user_input_elements[3])

        except ValueError as ve:
            print("\nInvalid position:", ve)

            return

        return instruction, [complex_number, position]

    return instruction, [complex_number]


def option_B_modify_numbers():

    print_option_B_modify_numbers_instructions()

    user_input = input("\n>")
    user_input = user_input.strip()
    user_input_elements = user_input.split(" ")
    instruction = user_input_elements[0]

    if len(user_input_elements) == 2:

        try:

            position = int(user_input_elements[1])

            return instruction, [position]

        except ValueError as ve:
            print("Invalid position:", ve)

    else:

        if instruction == "remove":

            instruction = instruction + "_between"
            start_position = int(user_input_elements[1])
            end_position = int(user_input_elements[3])

            return instruction, [start_position, end_position]

        else:

            old_number = get_complex_number(user_input_elements[1])
            new_number = get_complex_number(user_input_elements[3])

            return instruction, [old_number, new_number]


def option_C_display_numbers_having_different_properties():

    print_option_C_display_numbers_having_different_properties_instructions()

    user_input = input("\n>")
    user_input = user_input.strip()
    user_input_elements = user_input.split(" ")
    instruction = user_input_elements[0]

    if len(user_input_elements) == 1:

        return instruction, []

    else:

        instruction = instruction + "_" + user_input_elements[1]

        if user_input_elements[1] == "real":

            start_position = int(user_input_elements[2])
            end_position = int(user_input_elements[4])

            return instruction, [start_position, end_position]

        else:

            symbol = user_input_elements[2]
            number = float(user_input_elements[3])

            return instruction, [symbol, number]


def option_D_filter_the_list():

    print_option_D_filter_the_list_instructions()

    user_input = input("\n>")
    user_input = user_input.strip()
    user_input_elements = user_input.split(" ")
    instruction = user_input_elements[0]
    instruction = instruction + "_" + user_input_elements[1]

    if user_input_elements[1] == "real":

        return instruction, []

    else:

        symbol = user_input_elements[2]
        number = float(user_input_elements[3])

        return instruction, [symbol, number]


def option_E_undo():

    print_option_E_undo_instructions()

    return "undo", []


# menu
def print_menu_options():

    print("\n(A) Add a number")

    print("\n(B) Modify numbers")

    print("\n(C) Display numbers having different properties")

    print("\n(D) Filter the list")

    print("\n(E) Undo")


# run console
def run_console():

    list_of_complex_numbers = get_a_list_of_random_complex_numbers()
    list_of_lists_of_complex_numbers = [list_of_complex_numbers]

    options_dict = {"A": option_A_add_a_number,
                    "B": option_B_modify_numbers,
                    "C": option_C_display_numbers_having_different_properties,
                    "D": option_D_filter_the_list,
                    "E": option_E_undo,
                    }

    instructions_dict = {
        "add": add_a_complex_number_to_the_list,
        "insert": insert_a_complex_number_to_the_list,
        "remove": remove_a_complex_number_from_the_list,
        "remove_between": remove_complex_numbers_from_the_list_between_two_indexes,
        "replace": replace_a_complex_number_with_a_new_one,
        "list": print_list_of_complex_numbers,
        "list_real": print_real_numbers_from_list_of_complex_numbers_between_two_indexes,
        "list_modulo": print_complex_numbers_from_list_of_complex_numbers_by_modulo_expression,
        "filter_real": keep_in_the_list_only_the_complex_numbers_with_imaginary_part_zero,
        "filter_modulo": keep_in_the_list_only_the_complex_numbers_with_a_specific_modulo_property,
        "undo": undo_the_last_operation_on_the_list
    }

    while True:
        if list_of_lists_of_complex_numbers == []:
            list_of_lists_of_complex_numbers = [list_of_complex_numbers]

        print_menu_options()

        option_chosen = input("\nChosen option: ")

        try:
            chosen_instruction, arguments = options_dict[option_chosen]()

        except ValueError as ve:
            print("\nValue Error:", ve)
            continue

        except KeyError as ke:
            print("\nThis option doesn't exist:", ke)
            continue

        except IndexError as ie:
            print("\nInvalid instruction syntax:", ie)
            continue

        except TypeError as te:
            print("\nInvalid number of arguments:", te)
            continue

        try:
            if chosen_instruction == "undo":
                instructions_dict[chosen_instruction](list_of_lists_of_complex_numbers)
                continue

            list_of_complex_numbers = list_of_lists_of_complex_numbers[-1][:]
            instructions_dict[chosen_instruction](list_of_complex_numbers, *arguments)

            if list_of_complex_numbers != list_of_lists_of_complex_numbers[-1]:
                list_of_lists_of_complex_numbers.append(list_of_complex_numbers)

        except ValueError as ve:
            print("\nValue Error:", ve)

        except KeyError as ke:
            print("\nThis option doesn't exist:", ke)

        except TypeError as te:
            print("\nInvalid number of arguments:", te)

        except IndexError as ie:
            print("\nInvalid position index:", ie)
