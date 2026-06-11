"""
Lecture 4, week 4

Collections of data
    1. List []
        object containing multiple data items
        each item = element, with index (0~)
    2. Tuple ()
        immutable version of lists
        you can add on to tuple, but it does not modify the original set of element
        function that returns multiple values into single variable will become a tuples
    3. Dictionary
    4. Set
    5. Class
        one that we create by ourselves (done in the following week)

Sequence is an object that contains multiple data elements in order
    for python = lists, tuples, and strings
        lists = mutable
        tuples, and strings = immutable

List
    starts from 0
    from the right end starts from -1
del list[]
    deletes the following element by index
list.remove()
    removes the element by its value
    when there is same elements, only removes 1

methods for lists
    1. append()
        adds on to the end of the list
    2. sort()
        sort the element in ascending order
    3. reverse()
        reverses the order in the list
sorted()
    function that breaks a sequence into elements and sort the sequence returning as a list
    does not change the initial list and returns as a new list

from operator import itemgetter
    this allows us to sort using a different item inside each element

.split()
    splits the string, default using whitespace

", ".join(lists)
    joints each string using the following string

(*lists)
    this will unpack the list/tuples inside

list comprehension
    if we want to split the list and do the same thing, we can rather comprehend into a single line
        parts = data.split("/") # splits by "/"
        dob = tuple([int(part) for part in parts]) # make the list into a tuple
    standard shape
        [single for single in plural]
    calculations done on the left
        [single + 1 for single in plural]
    if statement done on right
        [single for single in plural if single > 5]
    for methods, some are done outside, changes the square bracket into bracket
    when you do not want to store the list, use bracket (generator expression)
    whe you want to store it, use square bracket (comprehension)
        max((single for single in plural))
    nested for loops are writen as a continuous for loops
        [x + y for x in range(1, 4) for y in range(1, 4)]
    same as
        things = []
        for x in range(1, 4):
            for y in range(1, 4):
                things.append(x + y)

Value equality x == y
    uses ==
    checks if the values are the same

Reference equality x is y
    uses is
    checks if the values refer to the same object in memory
    even it has the same data stored, if the memory (source) is different its false

alias/aliasing
    when there's a new variable referring to an existing list
    example:
        numbers = [10, 20, 30]
        more = numbers
        more.append(40)
    this will add 40 to both numbers and more
    to avoid this we can add the slice to the statement
    more = numbers[:]

id()
    this will show the memory of the following variable
    if it's the same, change of one will affect the other as well

optimization
    if the value is the same python sometimes automatically set into the same id
    but if 1 is modified, it doesn't affect to the other one, so the id would change
    applies until 256 for numbers, and short sting

"""

# Write a program that contains a (hard-coded) list of names. Ask the user which name they want to display
# as a number (1 = first name in the list), and then display it. Avoid any IndexError by using exception handling.

# names = ["Alex", "Alan", "Alon", "Alba", "Avalon"]
# try:
#     number = int(input(f"Name (1~{len(names)}): "))
#     print(f"Your chosen name is {names[number - 1]}")
# except IndexError:
#     print("Index Error, invalid input")

# Write a program for handling high scores that uses a nested list where the elements are [name, score] pairs.

# from operator import itemgetter
#
# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# new_student = input("Student name, Score: ")
# student_data = new_student.split(", ")
# student_data[1] = int(student_data[1])
# score_pairs.append(student_data)
# score_pairs.sort(key=itemgetter(1))
# print(score_pairs)

# Given a string called text, like: text = "This is a sentence"
# Write a list comprehension that produces a list of the words that have > 3 characters.

text = "This is a sentence"
words = text.split()
long_words = [word for word in words if len(word) > 3]
print(long_words)
