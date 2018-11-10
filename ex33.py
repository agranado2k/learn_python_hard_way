def generate_number_list(limit, delta = 1):
    i = 0
    numbers = []

    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + delta
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

def generate_number_list_for_loop_verstion(limit, delta = 1):
    numbers = []

    for i in range(0,limit, delta):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + delta
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    return numbers

# numbers = generate_number_list(6, 2)
numbers = generate_number_list_for_loop_verstion(6, 2)

print "The numbers:"

for num in numbers:
    print num
