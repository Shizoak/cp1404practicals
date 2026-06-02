"""
Create Random Number into .txt file
"""
from random import uniform


def main():
    number_of_random_value = int(input("How many values?: "))
    input_random_number(number_of_random_value)


def input_random_number(number_of_random_value):
    input_file = open("temps_input.txt", "w")
    for i in range(number_of_random_value):
        random_number = uniform(-200, 200)
        print(random_number, file=input_file)
    input_file.close()


main()
