"""
Practice Work, More Scores
"""
from random import randint


def main():
    number_of_score = int(input("Number of Scores: "))
    results = open("results.txt", "w")
    for i in range(number_of_score):
        random_score = get_random_score()
        random_grade = determine_grade(random_score)
        print(f"{random_score} is {random_grade}", file=results)
    results.close()


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def get_random_score():
    return randint(0, 100)


main()
