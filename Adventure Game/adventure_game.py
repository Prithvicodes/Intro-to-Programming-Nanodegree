import time
import random


def print_sleep(string):
    print(string)
    time.sleep(1)


def intro(item, villians):
    print_sleep("You find youself standing in an open field,\
filled with grass and yellow wildflowers.\n")
    print_sleep(f"Rumor has it that a {villians} is somewhere around here,\
and has been terrifying the nearby village.\n")
    print_sleep("In front of you is a house.\n")
    print_sleep("To your right is a dark cave.\n")
    print_sleep("In your hand you hold your trusty \
(but not very effective) dagger.\n")


def options(item, villians):
    print_sleep("Enter 1 to knock on the door of the house.\n")
    print_sleep("Enter 2 to peek into the cave.\n")
    print_sleep("What would you like to do?\n")
    choice = input("(Please enter 1 or 2.)\n")
    while True:
        if choice == '1':
            house(item, villians)
            break
        elif choice == '2':
            cave(item, villians)
            break
        else:
            choice = input("(Please enter 1 or 2.)\n")


def house(item, villians):
    print_sleep("You approach the door of the house.")
    print_sleep(f"You are about to knock when the door opens \
and out steps a {villians}.")
    print_sleep(f"Eep!This is the {villians}'s house!")
    print_sleep(f"The {villians} attacks you!")
    if "sword" not in item:
        print_sleep("You feel a bit under-prepared for this,\
What with only having a tiny dagger.")
    while True:
        choices = input("Would you like to (1) fight or (2) run away?")
        if choices == '1':
            if "sword" in item:
                fight_sword(item, villians)
                break
            else:
                fight_dagger(item, villians)
                break
        elif choices == '2':
            runaway(item, villians)
            break


def cave(item, villians):
    if "sword" in item:
        print_sleep("\nYou peer cautiously into the cave.")
        print_sleep("\nYou've been here before, and gotten all\
the good stuff. It's just an empty cave\
now.")
        print_sleep("\nYou walk back to the field.\n")
    else:
        print_sleep("You peer cautiously into the cave\n")
        print_sleep("It turns out to be only a very small cave.\n")
        print_sleep("Your eye catches a glint of metal behind a rock\n")
        print_sleep("You have found the magical Sword of Ogoroth!\n")
        print_sleep("You discard your silly old dagger and \
take the sword with you.\n")
        print_sleep("You walk back out to the field.\n")
        item.append("sword")
    options(item, villians)


def play_again():
    select = input("Would you like to play again? (y/n)").lower()
    if select == "y":
        print_sleep("Excellant!Restarting the game..\n")
        game_start()
    elif select == "n":
        print_sleep("Thanks for playing! See you next time.\n")
    else:
        play_again()


def fight_dagger(item, villians):
    print_sleep("You do your best...\n")
    print_sleep(f"but your dagger is no match for the {villians}.\n")
    print_sleep("You have been defeated!\n")
    play_again()


def fight_sword(item, villians):
    print_sleep(f"As the {villians} moves to attack,\
you unsheath your new sword.")
    print_sleep("The Sword of Ogoroth shines brightly in \
your hand as you brace yourself for the \
attack.")
    print_sleep(f"But the {villians} takes one look at \
your shiny new toy and runs away!")
    print_sleep(f"You have rid the town of the {villians}.\
You are victorious!\n")
    play_again()


def runaway(item, villians):
    print_sleep("You run back into the field.Luckily,\
you don't seem to have been followed.\n")
    options(item, villians)


def game_start():
    item = []
    villians = random.choice(['pirate', 'gorgon', 'troll', 'dragon'])
    intro(item, villians)
    options(item, villians)


game_start()
