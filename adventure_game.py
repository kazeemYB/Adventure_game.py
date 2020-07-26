import time
import random

villain = random.choice(["pirate", "troll", "fairie", "dragon", "gorgon"])
initialWeapon = random.choice(["dagger", "knife", "toothpick",
                               "wood-stick", "car-keys"])
victoryWeapon = random.choice(["sword", "relic", "rod",
                               "machine-gun", "bow & arrow"])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def restart_game():

    restart = input("Would you like to play again? (y/n)\n").lower()
    if restart != 'n' and restart != 'y':
        restart_game()
    elif restart == 'n':  # quits the game
        print_pause("Thanks for playing! See you next time.")
        # break
    elif restart == 'y':  # restarts the game
        print_pause("Excellent! Restarting the game ...")
        play_game()


def intro():

    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a wicked {villain} is somewhere around "
                "here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                f"(but not very effective) {initialWeapon}.")


def house():

    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a wicked {villain}.")
    print_pause(f"Eep! This is the wicked {villain}'s house!")
    print_pause(f"The wicked {villain} attacks you!")


def field(items):

    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")
    leapoffaith(items)


def fight(items):

    house()

    if f"{victoryWeapon}" in items:
        fight_or_run = input("Would you like to (1) fight or (2) run away? \n")
        while fight_or_run != '1' and fight_or_run != '2':
            fight_or_run = input("Would you like to (1) fight "
                                 "or (2) run away? \n")

        if fight_or_run == '2':
            field(items)

        elif fight_or_run == '1':  # you win the game
            print_pause(f"As the wicked {villain} moves to attack, "
                        f"you unsheath your new {victoryWeapon}.")
            print_pause(f"The {victoryWeapon} of Ogoroth shines brightly "
                        "in your hand as you brace yourself for the attack.")
            print_pause(f"But the wicked {villain} takes one look at "
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the wicked {villain}. "
                        "You are victorious!")
            restart_game()

    else:  # you lose the game
        print_pause("You feel a bit under-prepared for this, "
                    f"what with only having a tiny {initialWeapon}.")

        fight_or_run = input("Would you like to (1) fight or (2) run away? \n")
        while fight_or_run != '1' and fight_or_run != '2':
            fight_or_run = input("Would you like to (1) fight "
                                 "or (2) run away? \n")

        if fight_or_run == '1':  # you choose to fight without sword
            print_pause("You do your best...")
            print_pause(f"but your {initialWeapon} is no match "
                        f"for the wicked {villain}.")
            print_pause("You have been defeated!")
            restart_game()

        elif fight_or_run == '2':  # you choose to run away
            field(items)


def cave(items):

    if f"{victoryWeapon}" in items:  # you've been there before
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        leapoffaith(items)

    else:   # you picked up the sword in the cave
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause(f"You have found the magical {victoryWeapon} of Ogoroth!")
        print_pause(f"You discard your silly old {initialWeapon} and "
                    f"take the {victoryWeapon} with you.")
        print_pause("You walk back out to the field.")
        items.append(f"{victoryWeapon}")
        leapoffaith(items)


def leapoffaith(items):

    print_pause("Enter 1 to knock on the door of the house. \n"
                "Enter 2 to peer into the cave. \n"
                "What would you like to do?")
    house_or_cave = input("(Please enter 1 or 2.)\n")

    while house_or_cave != '1' and house_or_cave != '2':
        house_or_cave = input("(Please enter 1 or 2.)\n")

    if house_or_cave == '1':
        fight(items)
    elif house_or_cave == '2':
        cave(items)


def play_game():
    items = []
    intro()
    leapoffaith(items)


play_game()
