"""
A school teacher requires a small program that would allow primary school students to learn
about various number sequences. The teacher is interested in a simple menu-driven program
that has the following choices (where x and y are inputs the user enters once at the start
of the program):
"""

SEQUENCE_MENU_STRING = "1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n4. Exit the program"
first_number = 0
second_number = 0

print(SEQUENCE_MENU_STRING)
user_choice = int(input(">>> "))
while user_choice != 4:
    first_number = int(input("x: "))
    second_number = int(input("y: "))
    if user_choice == 1:
        if first_number % 2 == 0:
            for i in range(first_number, second_number + 1, 2):
                print(i, end=" ")

        else:
            for i in range(first_number + 1, second_number + 1, 2):
                print(i, end=" ")
    elif user_choice == 2:
        if first_number % 2 == 1:
            for i in range(first_number, second_number + 1, 2):
                print(i, end=" ")
        else:
            for i in range(first_number + 1, second_number + 1, 2):
                print(i, end=" ")
    elif user_choice == 3:
        for i in range(first_number, second_number + 1):
            squared_number = i ** 2
            print(squared_number, end=" ")
    else:
        print("Invalid Choice")
    print()
    print(SEQUENCE_MENU_STRING)
    user_choice = int(input(">>> "))
print("Finished. ")
