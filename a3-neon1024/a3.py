import random

import timeit

import sys

import os

def print_options():
    
    print("\nChoose options:\n")
    
    print("1: Generate a list of n random natural numbers\n   Generated numbers must be between 0 and 100.\n")
    
    print("2: Sort the list using the Cocktail Sort algorithm.\n")
    
    print("3: Sort the list using the Gnome Sort algorithm.\n")
    
    print("4. Sort for the Best Case.\n")
    
    print("5. Sort for the Average Case\n")
    
    print("6. Sort for the Worst Case\n")
    
    print("7: Exit the program.\n")


def print_list(list_to_be_printed: list):
    
    print("\n", list_to_be_printed)


def clear_list(list_to_be_cleared: list):
    
    list_to_be_cleared.clear()


def generate_a_list_of_n_random_natural_numbers(list_of_n_random_natural_numbers: list, n: int):
    
    clear_list(list_of_n_random_natural_numbers)
        
    for _ in range(0, n):

        list_of_n_random_natural_numbers.append(random.randint(0, 100))


def get_step():

    while True:
        
        step=int(input("\nStep: "))
        
        if step>0:
            
            return step
        
        else:
            
            print("Incorrect value for step. Try again.\n")


def sort_the_list_using_cocktail_sort_algorithm(list_of_n_random_natural_numbers: list, step: int):
    
    current_step=0
    
    start=0
    
    end=len(list_of_n_random_natural_numbers)-1
    
    swapped=1
    
    while swapped:
        
        swapped=0

        for i in range(start, end):
            
            if list_of_n_random_natural_numbers[i]>list_of_n_random_natural_numbers[i+1]:
                
                list_of_n_random_natural_numbers[i], list_of_n_random_natural_numbers[i+1]=list_of_n_random_natural_numbers[i+1], list_of_n_random_natural_numbers[i]
                
                swapped=1
            
            current_step+=1
                
            if current_step%step==0 and step>=0:
                        
                print_list(list_of_n_random_natural_numbers)
                        
                current_step=0
            
        if not swapped:
                
            return
            
        swapped=0
            
        end-=1
            
        for i in range(end-1, start-1, -1):
                
            if list_of_n_random_natural_numbers[i]>list_of_n_random_natural_numbers[i+1]:
                    
                list_of_n_random_natural_numbers[i], list_of_n_random_natural_numbers[i+1]=list_of_n_random_natural_numbers[i+1], list_of_n_random_natural_numbers[i]
                    
                swapped=1
                    
            current_step+=1
                
            if current_step%step==0 and step>=0:
                        
                print_list(list_of_n_random_natural_numbers)
                        
                current_step=0
                            
        start+=1
            
    if current_step and step>=0:
        
        print_list(list_of_n_random_natural_numbers)


def sort_the_list_using_gnome_sort_algorithm(list_of_n_random_natural_numbers: list, step: int):
    
    current_step=0
    
    index=0
    
    while index<len(list_of_n_random_natural_numbers):
        
        if index==0:
            
            index=1
            
        if list_of_n_random_natural_numbers[index]<list_of_n_random_natural_numbers[index-1]:
            
            list_of_n_random_natural_numbers[index-1], list_of_n_random_natural_numbers[index]=list_of_n_random_natural_numbers[index], list_of_n_random_natural_numbers[index-1]
            
            index-=1
            
        else:
            
            index+=1
            
        current_step+=1
        
        if current_step%step==0 and step>=0:
            
            print_list(list_of_n_random_natural_numbers)
            
            current_step=0
    
    if current_step and step>=0:
        
        print_list(list_of_n_random_natural_numbers)


def compute_execution_time_for_cocktail_sort_on_list(this_list: list):
    
    start_time=timeit.default_timer()
            
    sort_the_list_using_cocktail_sort_algorithm(this_list, -1)
                            
    print("\nTime taken for sorting the list with " + str(len(this_list)) + " elements: " + str(timeit.default_timer()-start_time))


def compute_execution_time_for_gnome_sort_on_list(this_list: list):
    
    start_time=timeit.default_timer()
            
    sort_the_list_using_gnome_sort_algorithm(this_list, -1)
                            
    print("\nTime taken for sorting the list with " + str(len(this_list)) + " elements: " + str(timeit.default_timer()-start_time))


def choose_sorting_algo_and_compute_execution_time_on_the_lists(a_list: list, b_list: list, c_list: list, d_list: list, e_list: list):
  
    while True:
                        
        print("Choose algorithm:\n")
                        
        print("1. Cocktail Sort\n")
                        
        print("2. Gnome Sort\n")
        
        chosen_algo=int(input("Chosen algorithm: "))
                        
        if chosen_algo == 1:
            
            compute_execution_time_for_cocktail_sort_on_list(a_list)
            
            compute_execution_time_for_cocktail_sort_on_list(b_list)
            
            compute_execution_time_for_cocktail_sort_on_list(c_list)
            
            compute_execution_time_for_cocktail_sort_on_list(d_list)

            compute_execution_time_for_cocktail_sort_on_list(e_list)

            break
                            
        elif chosen_algo == 2:

            compute_execution_time_for_gnome_sort_on_list(a_list)
            
            compute_execution_time_for_gnome_sort_on_list(b_list)
            
            compute_execution_time_for_gnome_sort_on_list(c_list)
            
            compute_execution_time_for_gnome_sort_on_list(d_list)
            
            compute_execution_time_for_gnome_sort_on_list(e_list)

            break
                            
        else:
            
            os.system("cls")
            
            print("\nInvalid option. Try again.\n")


def get_sorted_copy_of_list(this_list: list):
    
    copy_of_the_list=this_list[:]
    
    copy_of_the_list.sort()
    
    return copy_of_the_list


def exit_the_program():
    
    print("\nProgram has finished successfully.")
    
    sys.exit()


def choose_options():
    
    list_of_n_random_natural_numbers=[]
    
    step=0
                
    a_list=[]
                
    b_list=[]
                
    c_list=[]
                
    d_list=[]
                
    e_list=[]
    
    while True:
        
        print_options()
        
        option_chosen=int(input("Chosen option: "))
        
        if option_chosen>=1 and option_chosen<=7:
            
            if option_chosen==1:
                
                os.system("cls")
                
                print("\nGenerating a list of n random natural numbers...")
                
                n=int(input("\nn: "))
                
                generate_a_list_of_n_random_natural_numbers(list_of_n_random_natural_numbers, n)
                
                print("\nGenerated list of " + str(n) + " random natural numbers:")
                
                print_list(list_of_n_random_natural_numbers)
                
            elif option_chosen==2:
                
                    os.system("cls")
                
                    if list_of_n_random_natural_numbers==[]:
                        
                        print("\nGenerate a list first.")
                        
                    else:
                        
                        print("\nSorting the list using Cocktail Sort...")
                        
                        copy_of_the_list=list_of_n_random_natural_numbers[:]
                        
                        step=get_step()
                        
                        sort_the_list_using_cocktail_sort_algorithm(copy_of_the_list, step)
                    
            elif option_chosen==3:
                
                    os.system("cls")
                    
                    if list_of_n_random_natural_numbers==[]:
                        
                        print("\nGenerate a list first.")
                        
                    else:
                    
                        print("\nSorting the list using Gnome Sort...")
                    
                        copy_of_the_list=list_of_n_random_natural_numbers[:]
                        
                        step=get_step()
                        
                        sort_the_list_using_gnome_sort_algorithm(copy_of_the_list, step)
            
            elif option_chosen>=4 and option_chosen<=6:
                
                os.system("cls")
                
                print("\nSorting for a case...")
                
                list_len=int(input("\nInitial list length: "))
                
                generate_a_list_of_n_random_natural_numbers(a_list, list_len)
                
                generate_a_list_of_n_random_natural_numbers(b_list, list_len*2)
                
                generate_a_list_of_n_random_natural_numbers(c_list, list_len*4)
                
                generate_a_list_of_n_random_natural_numbers(d_list, list_len*8)
                
                generate_a_list_of_n_random_natural_numbers(e_list, list_len*16)
                
                if option_chosen==4:
                    
                    os.system("cls")
                    
                    print("\nSorting for the Best Case...\n")
                    
                    a_list_sorted_copy=get_sorted_copy_of_list(a_list)
                
                    b_list_sorted_copy=get_sorted_copy_of_list(b_list)
                    
                    c_list_sorted_copy=get_sorted_copy_of_list(c_list)
                    
                    d_list_sorted_copy=get_sorted_copy_of_list(d_list)
                    
                    e_list_sorted_copy=get_sorted_copy_of_list(e_list)
                    
                    choose_sorting_algo_and_compute_execution_time_on_the_lists(a_list_sorted_copy, b_list_sorted_copy, c_list_sorted_copy, d_list_sorted_copy, e_list_sorted_copy)
                    
                elif option_chosen==5:
                    
                    os.system("cls")
                    
                    print("\nSorting for the Average Case...\n")
                    
                    choose_sorting_algo_and_compute_execution_time_on_the_lists(a_list, b_list, c_list, d_list, e_list)
   
                
                elif option_chosen==6:
                    
                    os.system("cls")
                    
                    print("\nSorting for the Worst Case...\n")
                    
                    a_list_sorted_copy=get_sorted_copy_of_list(a_list)
                
                    b_list_sorted_copy=get_sorted_copy_of_list(b_list)
                    
                    c_list_sorted_copy=get_sorted_copy_of_list(c_list)
                    
                    d_list_sorted_copy=get_sorted_copy_of_list(d_list)
                    
                    e_list_sorted_copy=get_sorted_copy_of_list(e_list)

                    choose_sorting_algo_and_compute_execution_time_on_the_lists(a_list_sorted_copy[::-1], b_list_sorted_copy[::-1], c_list_sorted_copy[::-1], d_list_sorted_copy[::-1], e_list_sorted_copy[::-1])


            elif option_chosen==7:
                    
                os.system("cls")
                    
                exit_the_program()
            
        else:

            os.system("cls")
            
            print("\nInvalid option value. Try again.")


def main():
    
    os.system("cls")
      
    choose_options()


if __name__=="__main__":
    
    main()