"""
# in_file.read()
 read the entire content inside the file and then add up into single string file

# for line in in_file
 very good when you want to do the same thing on every line
 
# line.strip()
 strips whitespace from both starts and end of a string
 
# line.lstrip() and line.rstrip()
 removes only from the left or the right end
 
# in_file.read(n)
 specify number of bytes, 1 byte = 1 character
 
# in_file.readline()
 delivers only the line reading
 
# in_file.readlines()
 returns a list of all the lines form file
"""

# Read a file and print only the line staring with #

# FILE_NAME = "practice.txt"
# infile = open(FILE_NAME, 'r')
# for line in infile:
#     if line.startswith("#"):
#         print(line)
# infile.close()

"""
when using 'w', writing into a file
    1. if the file exists, it replaces (overwritten)
    2. if the file didn't exist, it creates its own

if want to addon to a file use 'a' which appends to the existing file

writing method
    1. print("", file=out_file)
    2. out_file.write(s)
        writes out string s to the file
    3. out_file.writelines(lines)
        writes list of strings to the file

open/close is always a pair its shortened using with
    1. with open(FILE_NAME, "w") as out_file 
"""

# Write a code to read a file, and print each part separately with the price formatted like currency

# with open("practice.txt", "r") as infile:
#     for line in infile:
#         parts = line.strip().split(",")
#         name = parts[0]
#         year = parts[1]
#         price = float(parts[2].strip("\\n"))
#         print(f"{name} is made in {year} and it costs ${price:.2f}")

"""
Try and Exception

if you want to print out the error message
    except ValueError as error:
        print(repr(error))

ways to deal exceptions
    1. look before you leap (LBYL)
    2. easier to ask forgiveness than permission (EAFP)
"""
