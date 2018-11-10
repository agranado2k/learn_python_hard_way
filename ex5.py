# -*- codgin: utf-8 -*-
name = 'Arthur Granado'
age = 37
height = 175 * 0.39 # cen
weight = 65 * 2.2 # kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "He's %d inches tall."% height
print "He's %d pounds heavy." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee."% teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
