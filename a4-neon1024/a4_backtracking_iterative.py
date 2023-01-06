def print_list_with_zeros_to_both_ends(solution: list):

    print("0", end=" ")

    for element in solution:

        print(element, end=" ")

    print("0")


def get_length_from_console():

    return int(input("Length (n): "))


def absolute_difference_between_consecutive_elements_is_either_1_or_2_and_first_element_is_not_zero(possible_solution: list):

    if possible_solution[0] == 0:

        return False

    for i in range(len(possible_solution) - 1):

        if abs(possible_solution[i + 1] - possible_solution[i]) not in [1, 2]:

            return False

    return True


def reached_desired_list_length_and_last_element_is_not_zero(possible_solution: list, solution_length: int):

    if len(possible_solution) == solution_length and possible_solution[-1] != 0:

        return True

    return False


def backtracking_iterative(solution_length: int, possible_values: list):

    possible_solution = [-2]  # candidate solution

    while len(possible_solution) > 0:

        element_was_chosen = False

        while not element_was_chosen and possible_solution[-1] < possible_values[-1]:

            possible_solution[-1] = possible_solution[-1] + 1  # increase the last component

            element_was_chosen = absolute_difference_between_consecutive_elements_is_either_1_or_2_and_first_element_is_not_zero(possible_solution)

        if element_was_chosen:

            if reached_desired_list_length_and_last_element_is_not_zero(possible_solution, solution_length):

                print_list_with_zeros_to_both_ends(possible_solution)

            elif len(possible_solution) < solution_length:

                possible_solution.append(-2)  # expand candidate solution

        else:

            possible_solution = possible_solution[:-1]  # go back one component


def main():

    subsequence_length = 2*get_length_from_console()+1

    possible_values = [-1, 0, 1]

    backtracking_iterative(subsequence_length-2, possible_values)    # solve for 0_..._0


if __name__ == "__main__":

    main()
