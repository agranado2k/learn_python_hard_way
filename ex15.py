# import move argv
from sys import argv

# get the arg when run the script
script, filename = argv

# open the file given filename
txt = open(filename)

# print the file name
print "Here's your file %r:" % filename
# prin the file content
print txt.read()

# print some string
print "Tyoe the filename again:"
# ask user to input some value
file_again = raw_input("> ")

# open the file given by user
txt_again = open(file_again)

# print the file content
print txt_again.read()
