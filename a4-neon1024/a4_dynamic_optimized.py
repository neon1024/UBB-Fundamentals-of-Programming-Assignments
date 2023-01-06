def get_length_from_console():

    return int(input("Length: "))


def ask_for_element_at_index(index: int):

    print("element " + str(index) + " : ", end="")


def get_list_from_console(list_length: int):

    new_list = []

    for index in range(list_length):

        ask_for_element_at_index(index)

        new_list.append(int(input()))

    return new_list


def get_sum_of_elements_in_list(this_list: list):

    elements_sum = 0

    for element in this_list:

        elements_sum += element

    return elements_sum


def absolute_minimum_difference_between_two_subsets(original_set: list, original_set_length: int, first_subset: list,
                                                    second_subset: list, first_subset_target: list,
                                                    second_subset_target: list, min_value: list, lookup: dict):

    absolute_difference_between_two_subsets = abs(get_sum_of_elements_in_list(first_subset) - get_sum_of_elements_in_list(second_subset))

    if original_set_length < 1:

        if absolute_difference_between_two_subsets < min_value[0]:

            min_value[0] = absolute_difference_between_two_subsets

            first_subset_target.clear()

            first_subset_target.extend(first_subset)

            second_subset_target.clear()

            second_subset_target.extend(second_subset)

        return absolute_difference_between_two_subsets

    key = (original_set_length, tuple(first_subset_target))

    if key not in lookup:

        # case 1: add the last element from original set only to the first subset and continue the search

        case_1_result = absolute_minimum_difference_between_two_subsets(original_set, original_set_length - 1,
                                                                        first_subset + [original_set[original_set_length - 1]],
                                                                        second_subset, first_subset_target,
                                                                        second_subset_target, min_value, lookup)

        # case 2: add the last element from original set only to the second subset and continue the search

        case_2_result = absolute_minimum_difference_between_two_subsets(original_set, original_set_length - 1,
                                                                        first_subset, second_subset + [original_set[original_set_length - 1]],
                                                                        first_subset_target, second_subset_target,
                                                                        min_value, lookup)

        lookup[key] = min(case_1_result, case_2_result)

    return lookup[key]


def main():

    original_set_length = get_length_from_console()

    original_set = get_list_from_console(original_set_length)

    first_subset = []

    second_subset = []

    minimum_value = [99999999999]

    lookup = {}

    print("\nAbsolute difference between subsets S1 and S2: " +
          str(absolute_minimum_difference_between_two_subsets(original_set, original_set_length, [], [], first_subset,
                                                              second_subset, minimum_value, lookup)))

    print("\nSubset S1: ")

    print(first_subset)

    print("\nSubset S2: ")

    print(second_subset)

    print("\nAbsolute difference between the sum of subsets: " + str(abs(get_sum_of_elements_in_list(first_subset) -
                                                                         get_sum_of_elements_in_list(second_subset))))


if __name__ == "__main__":

    main()
