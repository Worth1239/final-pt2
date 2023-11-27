import random


def game():
    print("Okay! Let us begin")
    y = input("What is your name? ")
    name = y

    print(f"Alright {name}, let's go!")
    print()
    print()
    print()
    print("You wake up at 7:00 AM, like always. You have work in a few hours, and you really don't feel like going")
    first_choice = input("What will you do? (A: Go to work, B: Don't go to work) ")
    if first_choice.upper() == "A":
        print("You get ready and go to work")
        a = input("How do you get to work? (A: Drive, B: Public transport/walk) ")
        print()
        if a.upper() == "A":
            print("You get into your 2004 Toyota corolla.")
            print()
            asd = [1, 2, 3, 4, 5, 6]
            bruh = random.choice(asd)
            if bruh == 1:
                print("You got into a car crash and died :(")
                print()
                print("You got the car crash ending!")
                quit()
                # ending
            else:
                print("You make it to the McDonalds and clock in.")

        elif a.upper() == "B":
            print("You hop on the bus and see there are seats in the front and back.")
            b = input("Where do you want to sit? (A:Front, B:Back) ")
            print()
            if b.upper() == "A":
                print("You take seat at the very front of the bus.")
                print("After a while, the bus fills up, and an old lady comes and asks for your seat.")
                print()
                c = input("What will you do? (A: Give up your seat, B: Stand on bidness) ")
                if c.upper() == "A":
                    print("You give your seat up and she thanks you.")
                    print("A stop before you get off, a man walks in with a gun and yells 'THIS IS A HIJACKING' and shoots you")
                    print()
                    print("You got the hijacking ending!")
                    quit()
                    # ending
                elif c.upper() == "B":
                    print("The people on the bus look at you weird and the grandma gets angry.")
                    d = input("What will you do? (A: ignore her, B: stand up and fight")
                    print()
                    if d.upper() == "A":
                        print("She walks away and asks someone else for their seat.")
                        print("You make it to the McDonalds and clock in.")
                    elif d.upper() == "B":
                        print("You stand up and roll your sleeves up")
                        print("The grandma gets so afraid that she has a heart attack and dies.")
                        print()
                        print()
                        print("You make it to the McDonalds and clock in.")
                    else:
                        print("Invalid, try again.")
                        quit()
                else:
                    print("Invalid, try again.")
                    quit()
            elif b.upper() == "B":
                print("You take a seat at the back of the bus")
                print()
            else:
                print("Invalid, try again.")
                quit()
        else:
            print("Invalid, try again.")
            quit()

    elif first_choice.upper() == "B":
        print("")
    else:
        print("Invalid, try again.")


x = input("Hello! Welcome to my story game! Would you like to play? ")
if x.lower() == "yes":
    game()
else:
    quit()
