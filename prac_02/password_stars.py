"""
write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
"""

password = input("Password: ")
for character in password:
    print("*", end="")

