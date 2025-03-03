'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''



# write a function that adds 1
# to the input and prints the result
def inc(a):

    # add one to the input
    a = a + 1

    # display the new value of a
    print(a) 
    

    # write a function that adds 1
# to the input and returns the result
def inc_return(a):

    a = a + 1

    return (a) # hint this is incomplete


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    # This variable stores the sum of the two inputs
    result = a + b

    return (result)


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    result = sum(a, b)

    result = inc_return(result)
    return result


# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    if a%2 == 0:
        return True
    else:
        return False


# create a for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    # hint: you can add strings together 
    # in order to concatenate them
    string = phrase

    for i in range (repeat - 1):
        string = string + phrase

    return string 