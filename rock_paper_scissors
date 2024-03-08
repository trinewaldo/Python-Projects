# rock, paper, scissors

import random

while True:
    game = ["rock", "paper", "scissors"]

    computer = random.choice(game)
    player = None

    while player not in game:
        player = input("Rock, Paper or Scissors?: ").lower()

    if player == computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("That was a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins; " + computer + " covers " + player)
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win; " + player + " crushes " + computer)
    elif player == "paper":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win; " + player + " covers " + computer)
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins; " + computer + " cuts " + player)
    else:
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("Computer wins; " + computer + " crushes " + player)
        else:
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win; " + player + " cuts " + computer)

    another_game = ["yes", "no"]
    play_again = None

    while play_again not in another_game:
        play_again = input("Play again...? (Yes/No): ").lower()

    if play_again != "yes":
        break
print("\nThat was Rock, Paper & Scissors for you!\nThank you!")
