# Solve the problem from the first set here

###############################################################################
# Problem 3
###############################################################################


def get_init_num():
    
    while True:
        
        init_num=int(input("Give me a natural number: "))
        
        if init_num>=0:
        
            return init_num


def get_num_of_digits_appearances(init_num):
    
    """
    This function returns a list where on each of its position it has the number
    of appearances of the correspondig number
    
    param init_num: integer
    return: 
    """
    
    num_of_digits_appearances=[]
    
    # initialize the digits list with 0
    
    for _ in range(0, 10):
        
        num_of_digits_appearances.append(0)
    
    # mark the number of appearances of each digit
    
    while init_num:
        
        num_of_digits_appearances[init_num%10]+=1
        
        init_num//=10
        
    return num_of_digits_appearances


def build_smallest_num_with_init_num_digits(num_of_appearances_of_digit):
    
    smallest_num=0
    
    digit=1
    
    # start building our number by finding the smallest digit that appears in
    # our initial number, different from 0
    
    while digit<10 and not num_of_appearances_of_digit[digit]:
        
        digit+=1
    
    smallest_num=smallest_num*10+digit
    
    num_of_appearances_of_digit[digit]-=1
    
    # then we add 0's if there are any
    
    while num_of_appearances_of_digit[0]:
        
        smallest_num*=10
        
        num_of_appearances_of_digit[0]-=1
    
    # we continue by adding the remaining digits from our initial number, in
    # ascending order, if there are any
    
    while digit<10:
        
        while num_of_appearances_of_digit[digit]:
            
            smallest_num=smallest_num*10+digit
            
            num_of_appearances_of_digit[digit]-=1
            
        digit+=1

    return smallest_num

def the_smallest_num_is_message(smallest_num):
    
    print("Smallest number is: " + str(smallest_num))


def main():
    
    init_num=get_init_num()

    # corner case: for 0 the smallest number is 0 and we're done

    if init_num==0:
        
        print("0")
        
        return

    # we use the list num_of_appearances_of_digit to store the number of appearances of each digit
    # in our initial number on the corresponding position in our list
    
    num_of_appearances_of_digit=get_num_of_digits_appearances(init_num)
    
    smallest_num=build_smallest_num_with_init_num_digits(num_of_appearances_of_digit)

    the_smallest_num_is_message(smallest_num)


if __name__=="__main__":
    
    main()