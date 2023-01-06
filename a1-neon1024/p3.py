# Solve the problem from the third set here

###############################################################################
# Problem 15
###############################################################################

def not_found_message(init_num):
    
    """
    This function gives out the message that there is no perfect number for the given value
    
    param init_num: integer
    return: message that informs us there is no perfect number for init_num
    """
    
    print("A perfect number for " + str(init_num) + " does not exists")


def is_perfect_num(possible_perf_num):
    
    """
    This function checks if we have a perfect number
    
    param possible_perf_num: integer
    return: 1 if possible_perf_num is a perfect number, 0 otherwise
    """
    
    if possible_perf_num<=0:
        
        return 0
    
    if possible_perf_num==1:
        
        return 1
    
    div_sum=1
    
    for possible_div in range(2, possible_perf_num//2+1):
        
        if possible_perf_num%possible_div==0:
            
            div_sum+=possible_div

    if possible_perf_num==div_sum:
        
        return 1
    
    return 0
    

def main():
    
    init_num = int(input("Give me a natural number: "))
    
    print()     # for newline

    while init_num < 0:

        print("The input provided is not a natural number\n")

        init_num = int(input("Give me a natural number: "))
    
    possible_perf_num=init_num-1
    
    if possible_perf_num<=0:
        
        not_found_message(init_num)
        
    else:
        
        found=0
        
        while not found:
            
            if is_perfect_num(possible_perf_num):
                
                print("The largest perfect number smaller than " + str(init_num) + " is: " + str(possible_perf_num))

                found=1
                
            else:
                
                possible_perf_num-=1
                
        if not found:
            
            not_found_message(init_num)


if __name__ == "__main__":
    
    main()