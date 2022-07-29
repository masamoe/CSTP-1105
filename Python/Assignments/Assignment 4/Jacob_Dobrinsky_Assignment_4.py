# Python Assignment 4
# 
# NOTE - RENAME ASSIGNMENT FILE yourname_Assignment_4.py
# DON'T FORGET THE UNDERSCORES _ IN YOUR FILE NAME
# Hand up only this file and not a folder nor the book.py file

"""
    1.) A file called book.py is included in this folder. It contains
    a string variable called paragraphs. Write code to do the following:
    - Import the book file as a module into this file

    In a single message print the following:
    - "There are X sentences in book."
    - "There are Y words in book."
      Note that hyphenated words e.g. "backward-compatible" count 
      as a single word and names, numbers and years count as
      words as well.
    - The last sentence from paragraph but replace all occurences
      of the word "and" with "&".
"""

print("\nQ 1.")
# Here I import the book module
import book

# define variables for the number of sentences by splitting at periods, 
# words by splitting at spaces, 
# and grab the final sentence by slicing between the second-to-last and last periods.
sentences_num = len(book.paragraphs.split(". "))
words_num = len(book.paragraphs.split(" "))
final_sentence = book.paragraphs[int(book.paragraphs.rindex(".", 0, -2)+2):]

# printing my variables in multiline and replacing the "and" with "&" in the final sentence
print(f"""There are {sentences_num} sentences in book. 
There are {words_num} words in book.
{final_sentence.replace("and", "&")}"""
)

"""
	2.) Tax Collector

	Write code that will ask the user, using an input, what their 
    monthly gross income is. If the user doesn't type in a number 
    print "ERROR not a number" and do not proceed with 
    the calculation.

    - If the user earns less than 500 dollars, the tax 
    taken is 0 and they are in the low tax bracket. Only for these 
    people should you do the following. Ask the user how many 
    children they have. For each child that they have, give them 
    10 dollars in child benefits. If the user does not type in a 
    number they get 0 dollars in child benefits.

    - If the user earns 500 dollars or more but less than  
    700 they are in the medium tax bracket. Tax taken 
    here should be 15% of any sum that is over 500.

    - If the user earns 700 dollars or more they are in the high 
    tax bracket. Tax taken here should be 15% of the sum that is 
    over 500 but less than 700 and 25% of everything over 700.

    The final result should show in a single print the user's 
    gross income, the tax bracket (low, medium or high), total 
    tax, child benefits and net income (gross + child benefits - 
    tax).

    Gross Salary = 400, Bracket = Low,    Tax = 0,     Child Benefits = 20, Net Income = 420, this user has 2 kids
    Gross Salary = 620, Bracket = Medium, Tax = 18,    Child Benefits = 0,  Net Income = 602
    Gross Salary = 905, Bracket = High,   Tax = 81.25, Child Benefits = 0,  Net Income = 823.75
"""

print("\nQ 2.")
# get monthly groos variable from user input
# defining variables which aren't used by all results as empty or zero
monthly_gross = input("What is your monthly gross salary? Answer: ")
kids_message = ""
child_benefit = 0

# try casting gross to float for calculations, if unable print error
try:
  monthly_gross = float(monthly_gross)
except:
  print("ERROR not a number")
  # if successful begin calculations with more or less the same operations as in JS
else:
  if monthly_gross < 500:
    children = int(input("How many children do you have? Answer:"))
    child_benefit = children*10
    tax = 0
    bracket = "Low"
    kids_message = f"This user has {children} kids."
  elif 500 <= monthly_gross < 700:
    tax = (monthly_gross-500)*0.15
    bracket = "Medium"
  else:
    tax = ((monthly_gross-500-(monthly_gross-700))*.15)+((monthly_gross-700)*.25)
    bracket = "High"
  
  # print final result in multiline for readablility, kids message will be empty if above Low Bracket
  print(f"""Result:
  Gross Salary = {monthly_gross}
  Bracket = {bracket}
  Tax = {tax}
  Child Benefits = {child_benefit}
  Net Income = {monthly_gross+child_benefit-tax}
  {kids_message}""")