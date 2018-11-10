# assing the number of cars to a variable
cars = 100

# assing the space in a car to a variable
space_in_a_car = 4

# assign the number of drivers to a variable
drivers = 30

# assign the number of passengers to a variable
passengers = 90

# assign the calculation for cars not driven to a variable
cars_not_driven = cars - drivers

# assign the calculation fo car driven to a variable
cars_driven = drivers

# assign the calculation of car poll capacity to a variable
carpool_capacity = cars_driven * space_in_a_car

# assign the calculation of the average passengers per car to a variable
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"

