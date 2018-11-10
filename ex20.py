# import module argv from lib sys
from sys import argv

# assign the script parameters
script, input_file = argv

# define function to print all file passing file as argument
def print_all(f):
    print f.read()

# define function to rewind pointer's file to begin passing file as argument
def rewind(f):
    f.seek(0)

# define function to print current line number and current file line
def print_a_line(line_count, f):
    print line_count, f.readline()

# open file and assign to variable
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
