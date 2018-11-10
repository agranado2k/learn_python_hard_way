ten_things = "Apple Oragnes Crwos Telephone Light Sugar"

print "Wait there's no 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do more things with stuff."

# print the second element in the list
print stuff[1]
# print the last element of the list
print stuff[-1] # whoa! fancy
# remove the last element o the list
print stuff.pop()
# convert list to string include space as separator
print ' '.join(stuff) # what? cool!
# convert list to string include as sperator the character '#'
print '#'.join(stuff[3:5]) # super stellar!
