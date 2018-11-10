# define function that will use the arguments to print some values
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!"% boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# call the funtion passing integers as arguments
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# define some variable and assign values
amount_of_cheese = 10
amount_of_crackers = 50

# call the function and pass the variavles as arguments (paramenters)
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
