#
# Write the implementation for A5 in this file
#
from math import sqrt


# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def string_contains_numbers(this_string: str):

    for number in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:

        if number in this_string:

            return True

    return False


def get_complex_number_from_console_list_representation():

    user_input = input()

    user_input = user_input.strip()

    complex_number_components = user_input.split(" ")

    number_of_components = len(complex_number_components)

    if number_of_components == 1:

        if 'i' in complex_number_components[0]:

            if not string_contains_numbers(complex_number_components[0]):

                return [0, int(complex_number_components[0][:-1] + "1")]

            else:

                return [0, int(complex_number_components[0][:-1])]

        else:

            return [int(complex_number_components[0]), 0]

    else:
        # number_of_components == 3

        if not string_contains_numbers(complex_number_components[2]):

            return [int(complex_number_components[0]),
                    int(complex_number_components[1] + complex_number_components[2][:-1] + "1")]

        else:

            return [int(complex_number_components[0]),
                    int(complex_number_components[1] + complex_number_components[2][:-1])]


#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def get_complex_number_from_console_dict_representation():

    user_input = input()

    user_input = user_input.strip()

    complex_number_components = user_input.split(" ")

    number_of_components = len(complex_number_components)

    if number_of_components == 1:

        if 'i' in complex_number_components[0]:

            if not string_contains_numbers(complex_number_components[0]):

                return {"real_part": 0, "imaginary_part": int(complex_number_components[0][:-1] + "1")}

            else:

                return {"real_part": 0, "imaginary_part": int(complex_number_components[0][:-1])}

        else:

            return {"real_part": int(complex_number_components[0]), "imaginary_part": 0}

    else:
        # number_of_components == 3

        if not string_contains_numbers(complex_number_components[2]):

            return {"real_part": int(complex_number_components[0]),
                    "imaginary_part": int(complex_number_components[1] + complex_number_components[2][:-1] + "1")}

        else:

            return {"real_part": int(complex_number_components[0]),
                    "imaginary_part": int(complex_number_components[1] + complex_number_components[2][:-1])}


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def get_longest_increasing_subsequence_of_complex_numbers_by_their_modulus(list_of_complex_numbers: list,
                                                                           list_of_complex_numbers_length: int):

    longest_increasing_subsequence_of_complex_numbers_by_their_modulus = []

    list_of_complex_numbers_modulus = []

    for complex_number in list_of_complex_numbers:

        list_of_complex_numbers_modulus.append(get_complex_number_modulus(complex_number))

        # list_of_complex_numbers_modulus.append(get_complex_number_modulus_dict_representation(complex_number))

    lis = [1]*list_of_complex_numbers_length

    for i in range(1, list_of_complex_numbers_length):

        for j in range(0, i):

            if list_of_complex_numbers_modulus[i] > list_of_complex_numbers_modulus[j] and lis[i] < lis[j] + 1:

                lis[i] = lis[j] + 1

    maximum = 0

    for i in range(list_of_complex_numbers_length):
        maximum = max(maximum, lis[i])

    while maximum != 0:

        for i in range(list_of_complex_numbers_length):

            if lis[i] == maximum:

                longest_increasing_subsequence_of_complex_numbers_by_their_modulus.append(list_of_complex_numbers[i])

                break

        maximum -= 1

    return longest_increasing_subsequence_of_complex_numbers_by_their_modulus


def get_complex_number_modulus(complex_number):

    if type(complex_number) == list:

        real_part = complex_number[0]

        imaginary_part = complex_number[1]

    else:

        real_part = complex_number["real_part"]

        imaginary_part = complex_number["imaginary_part"]

    return sqrt(real_part ** 2 + imaginary_part ** 2)


def get_longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10(list_of_complex_numbers: list,
                                                                               list_of_complex_numbers_length: int):
    longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10 = [list_of_complex_numbers[0]]

    current_subarray = [list_of_complex_numbers[0]]

    for index in range(1, list_of_complex_numbers_length):

        complex_number_modulus = get_complex_number_modulus(list_of_complex_numbers[index])

        if 0 <= complex_number_modulus <= 10:

            current_subarray.append(list_of_complex_numbers[index])

            if len(current_subarray) >= len(longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10):
                longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10 = current_subarray[:]

        else:

            if len(current_subarray) >= len(longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10):
                longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10 = current_subarray[:]

            current_subarray.clear()

    return longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#


def exit_program():

    print("\nProgram finished successfully.")

    quit()


def print_menu_options():
    print("\n1: Read a list of complex numbers (in z = a + bi form) from the console.\n")

    print("2: Display the entire list of numbers on the console.\n")

    print("3: Display the length and elements of a longest subarray of numbers where each number's modulus is in " +
          "[0, 10] range.\n")

    print("4: Display the length and elements of a longest increasing subsequence, when considering each number's " +
          "modulus.\n")

    print("5: Exit the program.\n")


def print_complex_number_to_console(complex_number):

    if type(complex_number) == list:

        real_part = complex_number[0]

        imaginary_part = complex_number[1]

    else:

        real_part = complex_number["real_part"]

        imaginary_part = complex_number["imaginary_part"]

    sign = " + " if imaginary_part >= 0 else " "

    if real_part == 0:

        if imaginary_part == 0:

            print("0")

        else:

            print(str(imaginary_part) + "i")

    else:

        if imaginary_part == 0:

            print(str(real_part))

        else:

            print(str(real_part) + sign + str(imaginary_part) + "i")


def print_the_length_and_elements_of_a_longest_increasing_subsequence_when_considering_each_numbers_modulus(
        longest_increasing_subsequence_of_complex_numbers_by_their_modulus: list):

    print("\nLength of the longest increasing subsequence of complex numbers by their modulus:")

    print(len(longest_increasing_subsequence_of_complex_numbers_by_their_modulus))

    print("\nElements of the longest increasing subsequence of complex numbers by their modulus:")

    for complex_number in longest_increasing_subsequence_of_complex_numbers_by_their_modulus:

        print_complex_number_to_console(complex_number)


def print_the_length_and_elements_of_a_longest_subarray_of_numbers_where_each_numbers_modulus_is_in_0_10_range(
        longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10: list):

    print("\nLength of a longest subarray of numbers where each number's modulus is in [0, 10] range: ")

    print(len(longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10))

    print("\nElements of a longest subarray of numbers where each number's modulus is in [0, 10] range: ")

    for complex_number in longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10:

        print_complex_number_to_console(complex_number)


def print_list_of_complex_numbers_to_console(list_of_complex_numbers: list):

    for complex_number in list_of_complex_numbers:

        print_complex_number_to_console(complex_number)


def ask_for_list_element_at_index(index: int):
    print("element " + str(index) + ": ")


def get_a_list_of_complex_numbers_from_console(list_of_complex_numbers: list, complex_numbers_to_read: int):

    for index in range(len(list_of_complex_numbers), len(list_of_complex_numbers) + complex_numbers_to_read):

        ask_for_list_element_at_index(index)

        # list_of_complex_numbers.append(get_complex_number_from_console_list_representation())

        list_of_complex_numbers.append(get_complex_number_from_console_dict_representation())

    return list_of_complex_numbers


def ask_how_many_complex_numbers_to_read_from_console():

    print("\nHow many complex numbers do you want to read from console?")

    print("\nComplex numbers to read from console: ", end="")


def menu(list_of_complex_numbers: list, list_of_complex_numbers_length: int):

    while True:

        print_menu_options()

        option_chosen = int(input("Option chosen: "))

        if option_chosen == 1:

            # Read a list of complex numbers (in z = a + bi form) from the console.

            ask_how_many_complex_numbers_to_read_from_console()

            complex_numbers_to_read = int(input())

            list_of_complex_numbers_length += complex_numbers_to_read

            list_of_complex_numbers = get_a_list_of_complex_numbers_from_console(list_of_complex_numbers[:],
                                                                                 complex_numbers_to_read)

        elif option_chosen == 2:

            # Display the entire list of numbers on the console.

            print_list_of_complex_numbers_to_console(list_of_complex_numbers)

        elif option_chosen == 3:

            # Display the length and elements of the longest subarray of numbers where each number's modulus is in
            # the [0, 10] range.

            longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10 = \
                get_longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10(list_of_complex_numbers[:],
                                                                                           list_of_complex_numbers_length)

            print_the_length_and_elements_of_a_longest_subarray_of_numbers_where_each_numbers_modulus_is_in_0_10_range(
                longest_subarray_of_complex_numbers_having_their_modulus_in_range_0_10)

        elif option_chosen == 4:

            # Display the length and elements of the longest increasing subsequence, when considering each number's
            # modulus

            longest_increasing_subsequence_of_complex_numbers_by_their_modulus = \
                get_longest_increasing_subsequence_of_complex_numbers_by_their_modulus(list_of_complex_numbers[:],
                                                                                       list_of_complex_numbers_length)

            print_the_length_and_elements_of_a_longest_increasing_subsequence_when_considering_each_numbers_modulus(
                longest_increasing_subsequence_of_complex_numbers_by_their_modulus)

        elif option_chosen == 5:

            # Exit the program

            exit_program()

        else:

            # Invalid option

            print("Invalid option. Try again.\n")


def main():

    list_of_complex_numbers_list_representation = [[1, 1],
                                                   [1, 2],
                                                   [1, 3],
                                                   [1, 4],
                                                   [1, 5],
                                                   [2, 1],
                                                   [2, 2],
                                                   [2, 3],
                                                   [2, 4],
                                                   [2, 5]]

    list_of_complex_numbers_dict_representation = [{"real_part": 1, "imaginary_part": 1},
                                                   {"real_part": 1, "imaginary_part": 2},
                                                   {"real_part": 1, "imaginary_part": 3},
                                                   {"real_part": 1, "imaginary_part": 4},
                                                   {"real_part": 1, "imaginary_part": 5},
                                                   {"real_part": 2, "imaginary_part": 1},
                                                   {"real_part": 2, "imaginary_part": 2},
                                                   {"real_part": 2, "imaginary_part": 3},
                                                   {"real_part": 2, "imaginary_part": 4},
                                                   {"real_part": 2, "imaginary_part": 5}]

    list_of_complex_numbers_length = 10

    # menu(list_of_complex_numbers_list_representation, list_of_complex_numbers_length)

    menu(list_of_complex_numbers_dict_representation, list_of_complex_numbers_length)


if __name__ == "__main__":

    print("Make magic happen")

    main()
