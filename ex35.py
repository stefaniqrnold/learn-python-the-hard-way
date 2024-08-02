from sys import exit

def goldRoom():
    while True:
        choice = input("This room is full of gold. How much do you take?\n> ")
        try:
            howMuch = int(choice)
            break
        except ValueError:
            print("Man, learn to type a number.")
    
    if howMuch < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bearRoom():
    print("There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?")
    bearMoved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bearMoved:
            print("The bear has moved from the door.\nYou can go through it now.")
            bearMoved = True
        elif choice == "taunt bear" and bearMoved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bearMoved:
            goldRoom()
        else: 
            print("I got no idea what that means.")

def cthulhuRoom():
    choice = input("Here you see the great evil Chtulhu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?\n> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhuRoom()

def dead(why):
    print(why, "Good job!")
    exit(0)
    
def start():
    choice = input("You are in a dark room.\nThere is a door to your right and left.\nWich one do you take?\n> ")

    if choice == "left":
        bearRoom()
    elif choice == "right":
        cthulhuRoom()
    else:
        dead("You stumble around the room until you starve.")

start()