"""Write pseudocode (an algorithm) to calculate how much a TV streaming service will cost per year based on a monthly subscription cost the user enters
from unicodedata import category"""

MONTH_PER_YEAR = 12

monthly_cost = float(input("Monthly Cost: "))
total_cost = monthly_cost * MONTH_PER_YEAR
print(f"The total cost is ${total_cost:.2f}")

"""Calculate user net pay after deducting tax"""

TAX = 0.10  # 10%

initial_pay = float(input("Initial Pay: "))
tax_pay = initial_pay * TAX
net_pay = initial_pay - tax_pay
print(f"Your net pay is ${net_pay:.2f}")

"""0-4 = baby5-17 = child18-65 = adult66+ = old"""

age = int(input("Age: "))
if age <= 4:
    category = "baby"
elif age < 18:
    category = "child"
elif age < 66:
    category = "adult"
else:
    category = "old"
print(f"Your age {age} is considered {category}")

"""Guessing secret number"""

SECRET_NUMBER = 5

guess_number = int(input("Guessing Number from 1-10: "))
while guess_number != SECRET_NUMBER:
    print("Wrong Guess")
    guess_number = int(input("Guessing Number from 1-10: "))
print("Correct!")

"""Adding age category"""

age = int(input("Users Age (0-120): "))
while age < 0 or age > 120:
    print("Invalid Age ><")
    age = int(input("Users Age (0-120): "))
if age < 5:
    category = "baby"
elif age < 18:
    category = "child"
elif age < 66:
    category = "adult"
else:
    category = "old"
print(f"Your age {age} is considered as {category}")

"""How many age to enter + total age"""

total_age = 0
number_of_people = int(input("How many people: "))
for i in range(1, number_of_people + 1):
    individual_age = int(input(f"How old is people number {i}: "))
    total_age += individual_age
print(f"There is {number_of_people} people in the room with total age of {total_age}")

"""Same but stop when -1"""

total_age = 0
total_people = 1
individual_age = int(input("How old is person number 1: "))
while individual_age != -1:
    total_age += individual_age
    total_people += 1
    individual_age = int(input(f"How old is person number {total_people}: "))
total_people -= 1
average_age = total_age / total_people
print(f"There is {total_people} people in the room with total age of {total_age} of average age {average_age}")

"""Which kind of loop should you use for the following scenarios (for=definite, while=indefinite)?"""

# Printing the even numbers from 16 to 100                = for
# Getting names until a blank one is entered              = while
# Reading every line in a text file                       = for
# Counting how many vowels there are in a sentence        = for
# Practising writing loops until you understand them well = while
