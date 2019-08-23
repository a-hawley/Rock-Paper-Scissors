from os import system, name
from random import choice

# List of computer's moves
commands = ["rock", "paper", "scissors"]


# Clear screen after text (ONLY WORKS IN TERMINAL, NOT IDLE -- COMMENT OUT AND REPLACE WITH 'print("\n" * 20)')
def clear_screen():
    system('cls' if name == 'nt' else 'clear')


def main():

    # Pseudo-random commands choice
    decision = choice(commands)
    # Condition to keep program running
    boolz = True
    # 'No' responses accepted
    n_list = ["n", "no", "exit"]
    # Welcome message
    print("Welcome to the game!  Type exit to end the game at any time.")
    # Begin loop
    while boolz:
        user = input("Choose rock, paper, or scissors:\n")
        if user.lower() == decision:
            print("Tie!")
        elif user.lower() == "exit":
            break
        elif user.lower() == commands[2] and decision == commands[0]:
            print("Rock smash scissors, you loose!")
        elif user.lower() == commands[2] and decision == commands[1]:
            print("Snip Snip!  You killed him to death.")
        elif user.lower() == commands[0] and decision == commands[1]:
            print("Somehow a piece of paper obliterates your rock.  Hmmm...")
        elif user.lower() == commands[0] and decision == commands[2]:
            print("You absolutely wreck the cheap plastic scissors.  Way to go.")
        elif user.lower() == commands[1] and decision == commands[0]:
            print("You float softly over rock, and suffocate it.  You win.")
        elif user.lower() == commands[1] and decision == commands[2]:
            print("Like a knife through butter, you're cut into tiny bits.  Not going very well.")
        else:
            print("Invalid input, try again!")
        # Opt player in/out
        replay = input("Do you want to play again?\n")
        if replay.lower() in n_list:
            break
        else:
            clear_screen()


# Run program
main()
