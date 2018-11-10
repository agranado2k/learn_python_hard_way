from sys import exit

def gold_room():
    """
    Produce the decision flow for the gold chamber.
    """

    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if 0 in next or 1 in next:
        how_much = next
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    """
    Produce the decision flow for the bear chamber.
    """

    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front o another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go thought it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no iddea what that means."

def cthulhu_room():
    """
    Produce the decision flow for cthulhu chamber.
    """

    print "Here you see the great evil Cthulhu."
    print "He, .it, whaterver stares at you an you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_roow()

def dead(why):
    """
    Finish the game.
    """

    print why, "Good job!"
    exit(0)

def start():
    """
    Intitialize the game.
    """

    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stuble around the romm until you starve.")


start()
