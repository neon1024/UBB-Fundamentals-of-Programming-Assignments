# 7. Generate all subsequences of length 2n+1, formed only by 0, -1 or 1, such that a1 = 0, ..., a2n+1= 0 and
# |ai+1 - ai| = 1 or 2, for any 1 ≤ i ≤ 2n.


def get_length_from_console():

    return int(input("Length (n): "))


def append_list_with_zeros(this_list: list, list_length: int):

    for _ in range(list_length):

        this_list.append(0)

    return this_list


def absolute_difference_between_consecutive_elements_is_either_1_or_2(solution_level: int, possible_solution: list):

    if abs(possible_solution[solution_level] - possible_solution[solution_level-1]) in [1, 2]:

        return True

    return False


def reached_desired_list_length_and_last_element_is_not_zero(solution_level: int, possible_solution: list, solution_length: int):

    if solution_level == solution_length and possible_solution[solution_length] != 0:

        return True

    return False


def backtracking_recursive(solution_level: int, possible_values: list, possible_solution: list, solution_length):

    if solution_level > solution_length:

        return

    for value in possible_values:

        possible_solution[solution_level] = value

        if absolute_difference_between_consecutive_elements_is_either_1_or_2(solution_level, possible_solution):

            if reached_desired_list_length_and_last_element_is_not_zero(solution_level, possible_solution, solution_length):

                print(possible_solution[1:])

            else:

                backtracking_recursive(solution_level + 1, possible_values, possible_solution, solution_length)


def main():

    possible_values = [-1, 0, 1]

    subsequence = []

    subsequence_length = 2*get_length_from_console()+1

    subsequence.append(0)   # start indexing from 1

    subsequence = append_list_with_zeros(subsequence[:], subsequence_length)

    backtracking_recursive(2, possible_values, subsequence[:], subsequence_length-1)    # solve for [2, 2*n]


if __name__ == "__main__":

    main()
