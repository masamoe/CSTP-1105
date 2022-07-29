# Python MultiLists

from operator import indexOf


multi_lists = [
	['A', 'B', 'C'],
	['D', 'E', 'F'],
	['G', 'H', 'I', 'J'],
]

"""
	1.) In separate prints, print out the A, D, E, I and J
	from multi_lists. Use the [][] system to access these values.
"""
print("\nQ 1.")

search_items = "ADEIJ"

for item in multi_lists:
	for letter in item:
		if letter in search_items:
			print(multi_lists[multi_lists.index(item)][item.index(letter)])

"""
	2.) Count the number of items that appear in the entire
	multi_lists. Print the sentence "There are X items 
	in multi_lists"
"""
print("\nQ 2.")

item_count = 0

for item in multi_lists:
	item_count += len(item)

print(item_count)


"""
	3.) Store the three tuples below in a list to create
	a multi dimensional collection variable. The loop through
	every item in this multidimensional collection and print 
	each one out. You will need to create a nested for loop.
"""
print("\nQ 3.")

tuple_a = ('one', 'two', 'three')
tuple_b = ('four', 'five', 'six')
tuple_c = ('seven', 'eight', 'nine')
tuple_list = [tuple_a, tuple_b, tuple_c]

for tuple_item in tuple_list:
	for item in tuple_item:
		print(item)


"""
	4.) Below is a multi dimensional list containing dictionaries.
	Loop through each one and print both the key and the value
	in each dictionary like so Key ~~ Value. When you encounter the 
	value "STOP"  stop printing anything else from the collection
	and exit out of all the loops
"""
print("\nQ 4.")

multi_dict = [
	{'BC': 'Vancouver', 'Ontario': 'Toronto', 'Alberta': 'Calgary'},
	{'Washington': 'Seattle', 'Oregon': 'STOP', 'Florida': 'Miami'},
	{'UK': 'London', 'Ireland': 'Dublin', 'France': 'Paris'}
]

for dict_item in multi_dict:
	for item in dict_item:
		if dict_item.get(item) == "STOP":
			quit()
		print(f"{item} ~~ {dict_item.get(item)}")
	

print("This print shows you have gotten to the end")

