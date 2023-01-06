# 3. Given the set of positive integers S, partition this set into two subsets S1 and S2 so that the difference
# between the sum of the elements in S1 and S2 is minimal. For example, for set S = { 1, 2, 3, 4, 5 },
# the two subsets could be S1 = { 1, 2, 4 } and S2 = { 3, 5 }. Display at least one of the solutions.


# Idea:
# sort the list
# add el[-1] to S1 and el[-2] to S2
# take one element from right to left beginning with el[-3] and put it in S1 or S2


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


def sort_list_ascending_using_bubble_sort(this_list: list):

    elements_swapped = True

    while elements_swapped:

        elements_swapped = False

        for i in range(len(this_list)-1):

            if this_list[i] > this_list[i+1]:

                this_list[i], this_list[i+1] = this_list[i+1], this_list[i]

                elements_swapped = True

    return this_list


def get_sum_of_elements_in_list(this_list: list):

    elements_sum = 0

    for element in this_list:

        elements_sum += element

    return elements_sum


def main():

    original_set_length = get_length_from_console()

    original_set = get_list_from_console(original_set_length)

    original_set = sort_list_ascending_using_bubble_sort(original_set)

    print("\nSubset S: " + str(original_set))

    first_subset = [original_set[-1]]

    second_subset = [original_set[-2]]

    for index in range(original_set_length - 3, -1, -1):

        if get_sum_of_elements_in_list(first_subset) + original_set[index] < get_sum_of_elements_in_list(second_subset)\
                                                                             + original_set[index]:

            first_subset.append(original_set[index])

        else:

            second_subset.append(original_set[index])

    print("\nSubset 1: " + str(first_subset))

    print("\nSubset 2: " + str(second_subset))

    print("\nAbsolute difference between the sum of subsets: " + str(abs(get_sum_of_elements_in_list(first_subset) -
                                                                         get_sum_of_elements_in_list(second_subset))))


if __name__ == "__main__":

    main()
