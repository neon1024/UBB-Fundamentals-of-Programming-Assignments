# Solve the problem from the second set here

###############################################################################
# Problem 10
###############################################################################

def palindrome(num):

    """
    This function computes and returns the palindrome of num

    param num: integer
    return pal: the palindrome of num
    """

    pal = 0

    while num != 0:

        pal = pal*10 + num%10

        num = int(num/10)

    return pal


if __name__ == "__main__":

    init_num = int(input("Give me a natural number: "))

    print() # for newline

    while init_num < 0:

        print("The input provided is not a natural number\n")

        init_num = int(input("Give me a natural number: "))

    print("The palindrome of the given natural number " + str(init_num) + " is: " + str(palindrome(init_num)))