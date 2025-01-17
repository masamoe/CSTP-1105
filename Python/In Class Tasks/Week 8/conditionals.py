# Python Conditionals

"""
	1.) Below, commented out, is an if else statement created with a
	lot of errors. Uncomment the code and fix the errors.
"""
print("\nQ 1.")

if 5 < 10:
	print("5 is less than 10")

else:
	print("5 is greater than 10")



"""
	2.) Use the bool variable called is_morning below and write an if else 
	statement that checks to see if is_morning is True. If it is True 
	then print "Good Morning". If it is False then print "Good Evening".
"""
print("\nQ 2.")

is_morning = True

if is_morning:
	print("Good Morning")
else:
	print("Good Evening")



"""
	3.) Create a bool called is_canadian and assign it a boolean value.
	Create another bool called has_blackH_hair and assign it a boolean value.
	Write a conditional statement that will print the sentence "You are
	Canadian and have black hair" if both bools are True. If not, don't
	print anything.
"""
print("\nQ 3.")

is_canadian = True
has_black_hair = False

if is_canadian and has_black_hair:
	print("You are Canadian and have black hair")



"""
	4.) Ask the user to type in their name (input). Write code to check
	and see if their name:
	- is over 6 characters long
	- contains the letter "a"
	- contains the letter "c"
	If all of the above are true print "You have a long name that contains a and c"
"""
print("\nQ 4.")

name = input("What is your name?")

if len(name) > 6 and "a" in name and "c" in name:
	print("You have a long name that contains a and c")

"""
	5.) Create a string called day and assign it a value of one of
	the names of the day of the week e.g. "Wednesday". Write a
	conditional statement that will check your variable and print
	either "X is a work day" or "X is a weekend day" where X is
	your day variable.
"""
print("\nQ 5.")

day = "Monday"
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

if day in weekdays:
	print(f"{day} is a work day")
else: print(f"{day} is a weekend day")

"""
	6.) The variable below called current_hour represents an
	hour on the 24 hour clock e.g. either 0 - 23. It is currently 
	commented out. Write code that
	asks the user to input a number between 0 and 23 to become
	currentHour. If this number cannot be turned into an int, 
	automatically assign it the value of 0. 
	
	Print the following based on the value of currentHour
	0 to 12 inclusive = "Morning time"
	13 to 16 inclusive = "Afternoon time"
	17 to 20 inclusive = "Evening time"
	21 to 23 inclusive = "Night time"
	any number < 0 or > 23 = "No time"

	Change the current_hour value to make sure all of your code
	is correct
"""
print("\nQ 6.")

current_hour = input("What hour (0-23) is it?: ")

try:
	current_hour = int(current_hour)
except:
	current_hour = 0
finally:
	if current_hour < 13:
		print("Morning Time")
	elif 13 <= current_hour < 17:
		print("Afternoon Time")
	elif 17 <= current_hour < 21:
		print("Evening Time")
	elif 21 <= current_hour < 24:
		print("Night Time")
	else:
		print("No Time")





"""
	7.) Below is a nested conditional statement - one where ifs
	are inside other ifs. It is written with some errors. Uncomment
	the code and fix it so that it will work correctly.
"""
print("\nQ 7.")

age = 23
has_honey = True

if age >= 19:
	print("You are old enough")
	if has_honey:
		print("You can buy alcohol")
	else:
		print("You cannot buy alcohol")
else:
	print("You are not old enough to buy alcohol")




"""
	8.) This question is similar to question 6 however this time
	you are dealing with an Am and PM clock time. The variable
	am_pm_time contains the value in a string "4pm"
	
	Print the following based on the value of current_hour
	12am to 12pm inclusive = "Morning time"
	1pm to 4pm inclusive = "Afternoon time"
	5pm to 8pm inclusive = "Evening time"
	9pm to 11pm inclusive = "Night time"

	Change the am_pm_time value to make sure all of your code
	is correct
"""
print("\nQ 8.")

am_pm_time = "120pm"
am_pm = am_pm_time[-2:]
time = am_pm_time.replace("pm", "").replace("am", "")

try:
	time = int(time)
except:
	print("Time Error")
else:
	if am_pm == "am" or am_pm_time == "12pm":
		print("Morning Time")
	elif 1 <= time < 5:
		print("Afternoon Time")
	elif 5 <= time < 9:
		print("Evening Time")
	elif 9 <= time < 11:
		print("Night Time")
	else:
		print("No Time")

