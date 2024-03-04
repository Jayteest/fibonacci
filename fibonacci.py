# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: October 30, 2023

# Description:
# This file contains the Fib_Sequence class. The class accepts an
# argument of a number of digits. It then iterates through the values
# of the Fibonacci Sequence, up to the max digits specified.

# Logic:
# class Fib_Sequence:
#   init:
#       n = 0
#       digits = passed argument
#       num1 = 0
#       num2 = 1
#   iter:
#       return self
#   next:
#       if n < digits:
#           value = num1
#           num1, num2 = num2, num1 + num2
#           n++
#           return value
#       else: raise StopIteration

# declare Fib_Sequence class
class Fib_Sequence():
    # initialization method for sequence
    def __init__(self, digits):
        # initialize iteration count to 0
        self.n = 0
        # initialize digits attribute to passed argument
        self.digits = digits
        # initialize first number to 0
        self.num1 = 0
        # initialize second number to 1
        self.num2 = 1

    # iter method to allow for iteration
    def __iter__(self):
        # return iterable
        return self

    # next method to call each iteration in sequence
    def __next__(self):
        # check that iteration count is within requested number of values
        if self.n < self.digits:
            # set value attribute to first number
            self.value = self.num1
            # set first number to value of second number and
            # set second number to sum of first and second numbers
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            # increment iteration count
            self.n += 1
            # return the value of current digit
            return self.value

        # if iteration has exceeded requested number of values...
        else:
            # raise a StopIteration exception
            raise StopIteration
