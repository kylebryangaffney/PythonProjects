# Python: 3.14.3
# Author: kyle gaffney
# Purpose: Demonstrating how to pass variables to and from functions

def start(nice=0, mean=0, name=""):
    """Entry point for the game. Initializes the game.

    Args:
        nice (int): The player's current nice score. Defaults to 0.
        mean (int): The player's current mean score. Defaults to 0.
        name (str): The player's name. Defaults to an empty string.
    """
    name = describe_game(name)
    nice, mean, name = nice_mean(nice, mean, name)

def describe_game(name):
    """Check if it is a new game or not.
        If new, get user name.
        Else thank the player for playing and continue.

    Args:
        name (str): Player's name. Or empty string if this is a new game.

    Returns:
        str: The player's name.
    """
    if name != "":
        print(f"\nThank you for playing again{name}")
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nPlease enter your name: ").capitalize()
                if name != "":
                    print(f"Welcome {name}")
                    print("In this game you will be greeted by several people\nYour choice is to be nice or mean")
                    print("Your actions have consequences")
                    stop = False
    return name

def nice_mean(nice, mean, name):
    """Prompt the player to choose between being nice or mean to a stranger,
    then update the score, then evaluate the result.

    Args:
        nice (int): The player's current nice score.
        mean (int): The player's current mean score.
        name (str): The player's name.

    Returns:
        tuple: Updated (nice, mean, name) values.
    """
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches for a conversation\nWould you like be nice(n) or mean(m)? Please only enter a single letter\n>>> ").lower()
        if pick == "n":
            print("The stranger walks away smiling\n")
            nice += 1
        if pick == "m":
            print("The stranger glares menacingly before storming off\n")
            mean += 1
        stop = False
    score(nice, mean, name)

def show_score(nice, mean, name):
    """Display the player's current nice and mean scores.

    Args:
        nice (int): The player's current nice score.
        mean (int): The player's current mean score.
        name (str): The player's name.
    """
    print(f"\n{name}, your current total is:\n\t{nice} Nice\n\t{mean} Mean")

def score(nice, mean, name):
    """Evaluate the current scores to determine whether the player has won,
    lost, or should continue playing.

    Args:
        nice (int): The player's current nice score.
        mean (int): The player's current mean score.
        name (str): The player's name.
    """
    if nice > 2:
        win(nice, mean, name)
    elif mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    """Display win message and play again promt.

    Args:
        nice (int): The player's final nice score.
        mean (int): The player's final mean score.
        name (str): The player's name.
    """
    print(f"\nWell done, {name}. Everyone liked you and you made friends on your journey.\n")
    again(nice, mean, name)

def lose(nice, mean, name):
    """Display a loss message and play again promt.

    Args:
        nice (int): The player's final nice score.
        mean (int): The player's final mean score.
        name (str): The player's name.
    """
    print(f"\nYou chose your path, {name}. You alienated people and there are consequences for your actions.\nLoss")
    again(nice, mean, name)

def again(nice, mean, name):
    """Promt player to play again. Resets the score if yes, or
    exits if no.

    Args:
        nice (int): The player's current nice score.
        mean (int): The player's current mean score.
        name (str): The player's name.
    """
    stop = True
    while stop:
        choice = input("\nWould you like to play again? (y/n)\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        elif choice == "n":
            print("Thank you for playing.\nWe hope to see you again.\n")
            stop = False
            quit()
        else:
            print("\nPlease enter only (Y) for yes or (N) for no")

def reset(nice, mean, name):
    """Reset the nice and mean scores to zero but not the player's name, then restart the game,
    
    Args:
        nice (int): The player's current nice score (will be reset to 0).
        mean (int): The player's current mean score (will be reset to 0).
        name (str): The player's name.
    """
    nice = 0
    mean = 0
    start(nice, mean, name)

if __name__ == "__main__":
    start()