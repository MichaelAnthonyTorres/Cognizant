import random
import time

location = ["New York", "LA", "Chicago", "Miami"]
guide = ["Mike", "John", "Kat", "Mel"]
name = input("Hello!! What is your name?").strip()  #looked up how to get rid of white space should someone enter a name such as "      alvin  "


def check_input(question, choice1, choice2):
    while True:
        response = input(question).lower()
        if choice1 in response:
            break
        if choice2 in response:
            break
        else:
            print("Sorry, could you say that again?")
    return response


def pause(message):
    print(message, flush=True)
    time.sleep(2)


def intro():
    pause(f"Hello {name}! My name is {random.choice(guide)}.")
    pause("I will be your guide today")
    pause(f"Welcome to {random.choice(location)}!!")


def visitor():
    response = check_input(
                            "Have you been here before?\n"
                            "Please say yes or no\n",
                            "yes", "no"
                )

    if "no" in response:
        pause("Oh wow first timer!! I hope your ready.")

    elif "yes" in response:
        pause("Well then, welcome back. I guess you know what you're in for.")

    pause("Ok then. Lets get going.")
    pause("First you must roll the dice to continue.")
    pause("We have to fight an enemy up ahead.")
    pause("The higher the number the better your chances.")
    pause("It is quite dangerous please think before you choose.")


def battle():
    enemy = ["Dragon", "Wizard", "Troll", "Chimera"]
    pause(f"You encounter a {random.choice(enemy)}. Can you defeat it?")


def dice_decision():
    strength = random.randint(1, 6)

    response = check_input(
        "Would you like to roll the dice\n"
        "Please say yes or no\n",
        "yes", "no"
    )

    if "yes" in response:
        pause("Brave soul you are. Ok lets roll the dice")
        pause(f"Ok you rolled a {strength}. That will be your strength")
        battle()
        if strength < 4:
            pause("Unfortunately you have been defeated.")

        elif strength >= 4:
            pause("You won. A statue was built of you in your honor.")

    elif "no" in response:
        pause(f"That's ok. Thanks for your honesty {name}")
    pause(f"That was quite an adventure {name}")
    restart()


def restart():
    response = check_input(
                            "Would you like to try again?\n"
                            "Please type yes or no\n",
                            "yes", "no"
                )

    if "yes" in response:
        pause("Ok here we go again")
        dice_decision()

    elif "no" in response:
        pause("Thanks for playing. See you again soon.")


def welcome():
    intro()
    visitor()
    dice_decision()


welcome()
