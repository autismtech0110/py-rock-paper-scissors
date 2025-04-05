# Play rock-paper-scissors against the computer!

# The random.choice() method allows you to pick an element at random, in this
# case from a list;
from random import choice

# sys.exit() is used to manually terminate execution of a program, in this
# case we will use it if a player enters invalid input, e.g. "Godzilla";
from sys import exit


# Throughout this program, I use many print() statements to enhance legibility
# in the terminal, e.g. below;
print()
print("This is Rock-Paper-Scissors! You will be playing against the\n" 
        "computer. Please enter your selection now...")
print()

# We use lower() to control for human error in the input, e.g. "ROCK";
human = input().lower()
print()

objects = ["rock","paper","scissors"]

# Check to make sure no invalid input was entered, if it was then terminate
# the program with sys.exit();
if human not in objects:
    print("This is invalid input, the game will now terminate. Please run\n"
            "the program from the beginning if you'd like to play again.")
    print()
    exit()

# We use random.choice() to randomly assign an element from objects to the
# computer;
computer = choice(objects).lower()

print(f"You chose {human}, and the computer chooses {computer}.")
print()


# Create a dictionary that will contain all possible winning combinations,
# from the human's perspective; ergo the keys are the human's choice, and the 
# subkeys are the computer's choice; if a particular combination is not found 
# in this dictionary, it means the human lost that round;
win_combos = {
        
        'rock': {'scissors': "Rock smashes scissors"},

        'paper': {'rock': "Paper covers rock"},

        'scissors': {'paper': "Scissors cut paper"}

}

# One of these messages gets tacked onto those from the dictionary, unless it 
# was a draw;
win_msg = ", therefore you win!"

lose_msg = ", therefore you lose!"

################# DECIDING WHO WINS

if human == computer:
    print(f"You and the computer both chose {human}, therefore it is a draw!")
    print()

# As stated above, if the combination of human and computer choices are in the 
# dictionary, that means the human won;
elif computer in win_combos[human]:
    print(win_combos[human][computer]+win_msg)
    print()

# And if the combination of human and computer choices are NOT in the
# dictionary, then that means the human lost; in this case, we would swap
# the key and subkey to get the appropriate message (value);
elif computer not in win_combos[human]:
    print(win_combos[computer][human]+lose_msg)
    print()

