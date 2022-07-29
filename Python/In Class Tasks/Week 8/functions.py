# Python Functions

"""
	1.) Below is a simple Python function that is created with errors. 
	Uncomment the code, fix the errors and make sure that the function 
	is called.
"""
print("\nQ 1.")

def say_hello():
	print("Hello World")

say_hello()



"""
	2.) Below is a Python function that uses parameters that is created
	with errors. Uncomment the code, fix the errors and call the function
	twice using the parameters 
"""
print("\nQ 2.")


def divide_number_by(num,divider):
	result = round(num / divider)
	print(f"{num} divided by {divider} is {result}")

divide_number_by(7, 2)



"""
	3.) Write a function that takes in 2 parameters. Both of these parameters
	should be numbers. Return a number that is both of the parameters multiplied
	together. If a parameter is not given then set its default value to be 0. 
	Test this function out on the following and call the function in
	a print() so that we can see the result:
	5, 5
	10, 7
	-12, 4
	8
"""
print("\nQ 3.")
def multiply_number_by(num,multiply):
	result = round(num * multiply)
	print(f"{num} multiply by {multiply} is {result}")

multiply_number_by(7, 2)


"""
	4.) Write a Python function that takes in 2 parameters, The first is 
	a string and the second is a number. Make this function return a new
	string that contains the first string printed the number of times as
	the second parameter dictated e.g. 'James', 3 would return
	'JamesJamesJames'
	Call this function on the following sets of parameters and print the 
	result to the console.
	Vancouver, 3
	XoXo, 10

"""
print("\nQ 4.")
def my_function(string,number):
	new_string = ""
	for num in range(number):
		new_string += string
	print(new_string)

my_function("Vancouver", 3)
my_function("XoXo", 10)


"""
	5.) Below is a list of letters with some letters being present more
	than once. Write a function that takes in a list as a parameter and
	returns a list that is sorted and has no duplicate items. Print 
	lettersList after it has passed through the function e.g.
	print( func_name( letters_list ) )
"""
print("\nQ 5.")

letters_list = ["A", "B", "C", "D", "B", "A", "F", "C", "A"]

def no_duplicates(letter):
	letter_set = set(letter)
	new_letters_list = list(letter_set)
	new_letters_list.sort()
	return new_letters_list

print(no_duplicates(letters_list))





"""
    6.) Write a function that takes in 2 parameters. The first is a list. 
    The second should be a string. The function should remove all items
    from the list that are equal to the second parameter e.g.
    list = ['A','A','B','B','C']
    second parameter = 'A'
    returned list = ['B','B','C']

    Remove all occurences of "dog" from the animal_list and print out
    the new "dog" free list.

"""
print("\nQ 6.")

animal_list = ["dog", "cat", "elephant", "dog", "tortoise", "cat", "dog", "horse", "elephant"]

def second_function(list = [],string =""):
	while string in list:
		list.remove(string)
	return list

print(second_function(animal_list,"dog"))


"""
	7.) Create a function that takes in a string parameter and returns
	a dictionary that contains the following keys and respective values:
	"word": the string passed in
	"number_of_chars": number of characters in string
	"has_capital": True or False whether string has a capital letter

	Test it out on the below variables
"""
print("\nQ 7.")

string_1 = "planet"
string_2 = "Hello"
def word_dict_function(para):
	my_dict = {"word": para , "number_of_chars": len(para) , "has_capital": False}
	my_list = "QWERTYUIOPASDFGHJKLZXCVBNM"
	for letter in para:
		if letter in my_list:
			my_dict["has_capital"] = True
	return my_dict

print(word_dict_function(string_1))
print(word_dict_function(string_2))

"""
	8.) Create a function that takes in a string parameter and returns
	a dictionary that contains the following keys and respective values:
	"word": the string passed in
	"number_of_chars": number of characters in string
	"has_capital": True or False whether string has a capital letter
	- You have done this above

	Create a function that takes in a list of strings and returns
	a new list that contains strings that are greater than 4 characters
	long and contain at least one capital letter.
	Hint: use the function you created above to help you here.
"""
print("\nQ 8.")

words_list = ["cat", "Monday", "Top", "help", "moNster", "lakE"]

def list_dict_function(para):
	new_list = []
	for item in para:
		my_dict = word_dict_function(item)
		if my_dict["has_capital"] == True and my_dict["number_of_chars"] > 4:
			new_list.append(item)
	return new_list

print(list_dict_function(words_list))
