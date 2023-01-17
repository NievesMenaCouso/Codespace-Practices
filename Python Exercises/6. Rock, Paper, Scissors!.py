from random import randint # This allows the computer to make random choices from a range
t = ["Rock", "Paper", "Scissors"] # Create a list with the options
computer = t[randint(0,2)] # Create a variable to store the computer's random choice
player = False # Create a boolean variable to store whether the player played (player==True, so computer's loop starts) or not yet (player==False, so computer waits)
while player == False: # Loop: While player has not moved (player==false), computer does nothing. When player moves (player==true) the "if" begins
 # The moment the player moves, set player to True the moment the player does their input
    player = input("Rock, Paper, Scissors?") # Player input
    if player == computer: # Ifs, quite self-explanatory
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False # At the end of the "if" commands we set the variable "player" back to false to stop the loop so the game can start again.
