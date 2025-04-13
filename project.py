from random import choices
from random import randrange
answer = choices
choices = ["1: Up", "2: Down", "3: Left", "4: Right"]
print("Hello, and welcome to my maze. In order to go into a direction select between 1-4.")
while True:
    player_guess = input("Choose your path: ")
    # Generate random number here
    answer = randrange(4)
    if player_guess.isnumeric():
        if int(player_guess) == 1:
            print("You go up")
        if int(player_guess) == 2:
            print("You go down")
        if int(player_guess) == 3:
            print("You go left")
        if int(player_guess) == 4:
            print("You go right")
        else:
            if int(player_guess) > 4:
                print("Please answer between 1 and 4")
    else:
        print("Please answer between 1 and 4")
    if (answer == int(player_guess)):
        print("You escaped!")
        break
    if (answer < int(player_guess)):
        print("You feel like you're getting farther from the exit..")
    else:
        print("You feel like you're getting closer to the exit")


