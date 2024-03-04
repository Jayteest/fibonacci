# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: October 30, 2023

# Description:
# This program tests the Fib_Sequence class. It prompts the user
# to enter the number of digits they would like. It then creates
# an instance of a Fib_Sequence object, and displays the requested
# number of digits from the Fibonacci Sequence.

# Logic:
# import fibonacci
# main:
#   get num values
#   sequence = Fib_Sequence(num values)
#   for i in sequence:
#       print(i)
# get num values:
#   prompt for values input
#   try: int(values input)
#   except: error message, go again
#   return values input

# import fibonacci.py to use Fib_Sequence class
import fibonacci

# declare main function
def main():
    # while loop to allow user to decide when they are done
    while True:
        # call get_num_values function to get number of fibonacci values wanted
        num_values = get_num_values()
        # check if no value was entered (ENTER)
        if not num_values:
            # if so, user is done, break from loop
            break
        
        # create Fib_Sequence object instance
        sequence = fibonacci.Fib_Sequence(num_values)

        # for loop to iterate through Fibonacci sequence
        for i in sequence:
            # display value
            print(f'{i}')

    # display exit message
    print(f'Goodbye!')

# function to get number of values input from user
def get_num_values():
    # loop for input validation
    while True:
        # prompt user for number of values they would like
        values_input = input(f'Enter the number of values you would like, '
                             f'or press ENTER to exit: ')
        # if user pressed enter, return a value of None
        if not values_input:
            return None

        # try suite to validate input
        try:
            # attempt to convert input to integer value
            values_input = int(values_input)
            # return integer value
            return values_input
        # if conversion to integer fails...
        except:
            # display error message
            print(f'Invalid entry. Please enter an integer value.')
            # continue to next loop iteration to try again
            continue

# call main to begin program execution         
if __name__ == '__main__':
    main()

    
