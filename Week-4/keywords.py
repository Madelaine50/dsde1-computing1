'''
keywords.py

Create functions that use keyword arguments
with default values.
'''
def welcome_message(a):
    keyword = a
    if keyword == '':
        print('space')
        return 'Hello world'
    
    else keyword == 'user_name':
        print('blessed')
        return 'Hello, <user_name>, and welcome'

    else keyword == 'place':
        print('beep')
        return 'Hello and welcome to <place>'

    else keyword == 'user_name' and 'place'
        print('hi')
        return 'Hello, <user_name>, and welcome to <place>'


welcome_message( )



welcome_message()
# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def list_average(list, avg_type)
    
    if avg_type == '' or 'mean':
        n = len(list)
        get_sum = sum(list)
        return mean = get_sum / n

    else avg_type == 'mode':
        import collections
        # calculating frequency of each value
        data = collections.Counter(list)
        mode = dict(data)
        return mode


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list