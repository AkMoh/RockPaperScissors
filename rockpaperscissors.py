# The computer will pick either rock paper scissors, can randomize that with the machine
# I will pick rock paper scissors
# Conditions:
# If I pick rock and they pick scissors, I win. If they pick paper, I lose. If they pick rock, it's a draw.
# If I pick scissors and they pick paper, I win. If they pick rock, I lose. If they pick scissors, it's a draw.
# If I pick paper and they pick rock, I win. If they pick scissors, I lose. If they pick paper, it's a draw.
# Once the game has started, the computer will have a choice in mind, then I will be presented with the 3 options.
# I make my choice and it is compared to the computer's choice.
# Check earlier conditions
# No matter the outcome the computer will select a new random choice.
# Score will be tallied
import random

print("Welcome to Rock, Papers, Scissors!")
options = ("r", "p", "s")

my_score = 0
opp_score = 0

is_Running = True

while is_Running:

    opponent = random.choice(options)
    choose = input("Rock, Paper, or Scissors? (r, p, s) (q to quit): ").lower()
    if choose == "r":
        print("Your choice: Rock")
        if opponent == "s":
            print("Opponent choice: Scissors\nYou win!")
            my_score += 1
        elif choose == opponent:
            print("Opponent choice: Rock\nTie!")
            continue
        elif opponent == "p":
            print("Opponent choice: Paper\nYou lose!")
            opp_score += 1
            continue
    elif choose == "p":
        print("Your choice: Paper")
        if opponent == "r":
            print("Opponent choice: Rock\nYou win!")
            my_score += 1
        if choose == opponent:
            print("Opponent choice: Paper\nTie!")
            continue
        elif opponent == "s":
            print("Opponent plays scissors.\nYou lose!")
            opp_score += 1
            continue
    elif choose == "s":
        print("Your choice: Scissors")
        if opponent == "p":
            print("Opponent choice: Paper\nYou win!")
            my_score += 1
        elif choose == opponent:
            print("Opponent choice: Scissors\nTie!")
            continue
        elif opponent == "r":
            print("Opponent plays rock.\nYou lose!")
            opp_score += 1
            continue
    elif choose == "q":
        print(f"Your score: {my_score}\nOpponent score: {opp_score}")
        is_Running = False
    else:
        print("Invalid option.")
