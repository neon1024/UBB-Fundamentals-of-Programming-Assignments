import random

import sys

import os

def print_options():
    
    print("\n1: Generate a list of n random natural numbers\n   Generated numbers must be between 0 and 100.\n")
    
    print("2: Sort the list using the Cocktail Sort algorithm.\n")
    
    print("3: Sort the list using the Gnome Sort algorithm.\n")
    
    print("4: Exit the program.\n")


def print_list(list_to_be_printed):
    
    print("\n", list_to_be_printed)


def clear_list(list_to_be_cleared):
    
    list_to_be_cleared.clear()


def generate_a_list_of_n_random_natural_numbers(list_of_n_random_natural_numbers, n):
    
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


def sort_the_list_using_cocktail_sort_algorithm(list_of_n_random_natural_numbers, step):
    
    step=get_step()
    
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
                
            if current_step%step==0:
                        
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
                
            if current_step%step==0:
                        
                print_list(list_of_n_random_natural_numbers)
                        
                current_step=0
                            
        start+=1
            
    if current_step:
        
        print_list(list_of_n_random_natural_numbers)


def sort_the_list_using_gnome_sort_algorithm(list_of_n_random_natural_numbers, step):
    
    step=get_step()
    
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
        
        if current_step%step==0:
            
            print_list(list_of_n_random_natural_numbers)
            
            current_step=0
    
    if current_step:
        
        print_list(list_of_n_random_natural_numbers)


def exit_the_program():
    
    os.system("cls")
    
    print("\nProgram has finished successfully.")
    
    sys.exit()


def choose_options():
    
    list_of_n_random_natural_numbers=[]
    
    step=0
    
    while True:
        
        print_options()
        
        option_chosen=int(input("Choose option: "))
        
        if option_chosen>=1 and option_chosen<=4:
            
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
                        
                        sort_the_list_using_cocktail_sort_algorithm(copy_of_the_list, step)
                    
            elif option_chosen==3:

                    os.system("cls")
                    
                    if list_of_n_random_natural_numbers==[]:
                        
                        print("\nGenerate a list first.")
                        
                    else:
                    
                        print("\nSorting the list using Gnome Sort...")
                    
                        copy_of_the_list=list_of_n_random_natural_numbers[:]
                        
                        sort_the_list_using_gnome_sort_algorithm(copy_of_the_list, step)
                    
            elif option_chosen==4:
                
                exit_the_program()
            
        else:
            
            os.system("cls")
            
            print("\nInvalid option value. Try again.")


def main():

    os.system("cls")        

    choose_options()


if __name__=="__main__":
    
    main()