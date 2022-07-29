# Python Assignment 5
# 
# NOTE - RENAME ASSIGNMENT FILE yourname_Assignment_5.py
# DON'T FORGET THE UNDERSCORES _ IN YOUR FILE NAME
# Hand up only this file and not a folder nor the accompanying module file 
# assignment5ModuleContainingVariables.py
import assignment5ModuleContainingVariables as a5_mod

"""
    1.) Making a Tuple of Numbers
    Write a function called 

    divisible_numbers() 

    that takes in two number parameters. The first parameter
    represents the start number and the second represents the end number.
    The first parameter will always be smaller than the second parameter
    so there is no need to check or constrain this.
    This function should RETURN a tuple of all the numbers between these
    numbers (including the start and end numbers themselves if applicable) 
    that are divisible by either the number 3, 5 or 7. That means if I divide 
    the number by either 3 or by 5 or by 7 it shouldn't leave a remainder.
    The modulo operator % will come in handy here https://stackoverflow.com/questions/4432208/what-is-the-result-of-in-python
    as will using casting to transform a collection of one type into another.
    
    EXAMPLE
    ParameterA = 2,  ParameterB = 14, Result = (3, 5, 6, 7, 9, 10, 12, 14)
    ParameterA = -5, ParameterB = 5 , Result = (-5, -3, 0, 3, 5)
"""
print("\nQ 1.")

def divisible_numbers(start_num, end_num):
    number_list = []
    for num in range(start_num, end_num+1):
        if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            number_list.append(num)
    return tuple(number_list)

print(divisible_numbers(2, 14))
print(divisible_numbers(-5, 5))


"""
	2.) Returning True of False
    Write a function called 

    no_hyphen_only_lower() 

    that takes in a string as a parameter. This function 
    should RETURN a boolean True if the string contains only lowercase letters
    and does not contain a hyphen "-".
    It should return False if there are any uppercase letters present or if 
    there are any hyphens "-" present.
    EXAMPLE
    Parameter = "james",     Result = True
    Parameter = "Mark",      Result = False
    Parameter = "ann-marie", Result = False

    Use this function to count the number of items in the question_two_multi_list
    variable that is stored in the accompanying module that contain only lowercase 
    letters without any hyphens. Each list item is a single word or single hyphenated word.

    Finally PRINT a sentence that reads "There are X lowercase no-hyphen words
    in the list" where X is the counted number.

    EXAMPLE
    test_list = [
        ["bakery", "Lions", "ice-cream", "caT", "sunday", "marKET"],
        ["drive-through", "Inspired", "haze"]
    ]
    Result = "There are 3 lowercase no-hyphen words in the list"

"""
print("\nQ 2.")

def no_hyphen_only_lower(str_para):
    no_cap_no_hyph = False
    if str_para.islower() and "-" not in str_para:
        no_cap_no_hyph = True
    return no_cap_no_hyph
        
def list_checker(list_para):
    item_counter = 0
    for sub_list in list_para:
        for word in sub_list:
            if no_hyphen_only_lower(word):
                item_counter += 1
    return item_counter

print(f"There are {list_checker(a5_mod.question_two_multi_list)} lowercase no-hyphen words in the list.")

            

"""
    3.) Dictionary of Counted Words
    Write a function called 

    most_used_words() 

    that takes in a string as a parameter and returns a dictionary containing
    any word that appears more than 4 times in the string. The
    word should be in lowercase and appear as the the dictionary key 
    and its value should be
    an integer representing the amount of times it appears. The
    order these words appear in the dictionary does not matter.
    The casing of the word should not matter either e.g. cat is
    the same as CAT and should be counted together.

    Use this function to return a dictionary on the snippet
    of text from the 1840 Canadian Act of Union which is 
    stored in the accompanying module.
    
    EXAMPLE
    Parameter = "Cat story. The cat in the cat ville, had the sister cat, who's name was the cat-like name called Cat. All the cats loved being a cat.",     
    Result = {'cat': 6, 'the': 5}

    NOTE in the code above, "cat-like" was not considered "cat" neither
         was "cats" because of the "s" at the end. 

"""
print("\nQ 3.")

def most_used_words(string_para):
    for word in string_para:
        