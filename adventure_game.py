import time

import random


def print_pause(msg):
    print(msg)
    time.sleep(2)


def intro(item, option):
    print_pause("In the valley of Bimra between the mountains of Korhen,\n")
    print_pause("A river flowing right across river is the Black forest.\n")
    print_pause("People of Bimra could never cross the river.\n")
    print_pause("The " + option + " would kill anyone entering the forest.\n")
    print_pause("The " + option + " has been scaring people in the valley.\n")
    print_pause("In front of you is the bridge,\n")
    print_pause("to cross the river into the forest.\n")
    print_pause("You are a famous monster hunter,\n")
    print_pause("and the people of the valley have asked your help,\n")
    print_pause("to get them rid of the monster in the black forest.\n")
    print_pause("To your right is the local swordsmith shop.\n")
    print_pause("You are equipped with an old sword and a smoke dynamite\n")
    print_pause("and in your pouch you also have some gold coins.\n")


def shop(item, option):
    if "sword" in item:
        print_pause("\nYou go to see the swordsmith to buy a new sword.")
        print_pause("\nYou have been here before, and equipped the weapon")
        print_pause("\nYou walk back to the valley.\n")
    else:
        print_pause("\nYou go to see the swordsmith in the shop.")
        print_pause("\nThe swordsmith greets and ask if he can help.")
        print_pause("\nYou look around the shop and see all kinds of swords.")
        print_pause("\nYou come across and find a silver sword!")
        print_pause("\nYou buy the Sword with coins ")
        print_pause("\nand exchange your old sword with a crossbow.")
        print_pause("\nYou walk back out to the valley.\n")
        item.append("sword")
    field(item, option)


def bridge(item, option):
    print_pause("\nYou cross the river over the bridge and enter the forest.")
    print_pause("\nYou see a cabin where the " + option + " could be living.")
    print_pause("\nYou inspect around the cabin and it seems nobody is here.")
    print_pause("\nYou enter the cabin......\n")
    print_pause("\nYou see rotten human flesh on the ground!")
    print_pause("\nWhile inspecting the place you turn around...")
    print_pause("\nand see the " + option + " standing behind you!")
    print_pause("\nThe " + option + " attacks you!\n")
    if "sword" not in item:
        print_pause("You are shocked and not fully prepared for this, "
                    "You unsheath out your sword anyways.\n")
    while True:
        choice2 = input("Would you (1) fight or (2) "
                        "throw smoke at the " + option + " and run away?")
        if choice2 == "1":
            if "sword" in item:
                print_pause("\nAs the " + option + " moves to attack,"
                            "You unsheath your Silver sword!\n")
                print_pause("\nYou let the " + option + " make it's move ")
                print_pause("\nand you brace yourself for the attack.")
                print_pause("\nAs the " + option + " tries to attack you ")
                print_pause("\nYou dodge the attack and swing your sword")
                print_pause("\nAnd shoot the crossbow, hitting it in the eye")
                print_pause("\nThe " + option + " screams and steps forwards")
                print_pause("\nYou swing the sword at the " + option + ".")
                print_pause("\nIt's head falls down from its neck")
                print_pause("\nYou have finally killed the " + option + ".")
                print_pause("\nYou fought bravely and defeated the monster!\n")
                print_pause("\nCongratulations!\n")
            else:
                print_pause("\nYou fought bravely and with courage but...")
                print_pause("\nyour sword broke while fighting the monster")
                print_pause("\nYou have been defeated\n")
                print_pause("\nGAME OVER\n")
                print_pause("\nTry one more time\n")
            play_again()
            break
        if choice2 == "2":
            print_pause("\nYou run back to the valley.\n"
                        "\nFortunatley, you are save and have not been "
                        "followed.\n")
            field(item, option)
            break


def field(item, option):
    print_pause("Press 1 to cross the river and enter the Blackforest.")
    print_pause("Press 2 to visit the Swordsmith.\n")
    print_pause("What would you do?\n")
    while True:
        choice1 = input("(Please press 1 or 2)\n")
        if choice1 == "1":
            bridge(item, option)
            break
        elif choice1 == "2":
            shop(item, option)
            break


def play_again():
    again = input("Play again? (yes/no)").lower()
    if again == "yes":
        print_pause("\n\n\nGet ready! Restarting the game ...\n\n\n")
        play_game()
    elif again == "no":
        print_pause("\n\n\nThanks for fighting! See you again soon .\n\n\n")
    else:
        play_again()


def play_game():
    item = []
    option = random.choice(["Djinn", "Vampire", "Red dragon", "Witch",
                            "Wolverine", "One-eyed ogre"])
    intro(item, option)
    field(item, option)


play_game()
