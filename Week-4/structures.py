'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):

    a_list = the_list[0:-1]
    return a_list



# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):

    if end < beginning :
        raise ValueError # hint this is incomplete

    if beginning > len(the_list) or end > len(the_list):
        raise ValueError
    
    #create new list
    new_list = the_list[beginning - 1 : end - 1]

    # reverse new list
    new_list = new_list[::-1]

    return new_list



# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    the_list.insert(index + 1, index) 
    the_list.insert(index + 1, index)

    return the_list


# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    if word == word[::-1] :
        print('true')
        return 
    else:
        print('false')
        return 

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    
    sentence = sentence.lower()
    import string

    #sentence = sentence.translate(None, string.punctuation)

    print(sentence)
    sentence = sentence.replace(" ", "")

    if sentence == sentence[::-1]:
        print('reads backwards')
        return 
    else:
        print('does not read backwards')
        return 
        

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence. 
def concatenate_sentences(sentenece1, sentence2):

    sentence = sentenece1.replace(" ", "")
    print(sentence)
    print(sentence[-1:])
    if sentence[0] != sentence[0].upper():
        print('doesnt start with capital letter ')
        return 
    elif sentence[-1:] != '.' or sentence[-1:] != '?' or sentence[-1:] != '!':
        print('does not have specified punctuation')
        return 
    second = sentence2.replace(" ", "")
    concat = sentence + ' ' + second
       


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False


# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
#Checks whether value is in the dictionary
    if value in dictionary:
        print('true')
        return True
    else:
        print('false')
        return False 




# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary3 = {**dictionary1, **dictionary2}
    print(dictionary3)
    return



