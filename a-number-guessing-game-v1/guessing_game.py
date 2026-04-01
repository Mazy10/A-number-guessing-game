"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

# Import the random and statistics modules.
import statistics
import random

def start_game():
    print("welcome to the guessing game")
    guesses_list = []
    play_again = "y"

    while play_again == "y":
        winning_number = random.randint(1,10) 
        guesses = 0   
        while True:
            guess = int(input("What is the correct number? "))
            guesses += 1
            if guess > winning_number:
                print("it's lower")
            elif guess < winning_number:
                print("it's higher")
            else:
                print("Got it")
                guesses_list.append(guesses)
                print(f'The number of guesses it took you was: {guesses}')
                print(f'The mean of the number of attempts was: {statistics.mean(guesses_list)}')
                print(f'The median of the number of attempts was: {statistics.median(guesses_list)}')
                print(f'The mode of the number of attempts was: {statistics.mode(guesses_list)}')
                print(guesses_list)
                break
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            continue
        else:
            print("Thanks for playing! See you again soon.")
            break


start_game()


# Create the start_game function.
# Write your code inside this function.
  
   #   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.

#   2. Store a random number as the answer/solution.
    
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".
#   4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
        
#   5. Display the following data to the player
#     a. How many attempts it took them to get the correct number in this game
#     b. The mean of the saved attempts list
#     c. The median of the saved attempts list
#     d. The mode of the saved attempts list
#   6. Prompt the player to play again
#     a. If they decide to play again, start the game loop over.
#     b. If they decide to quit, show them a goodbye message.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
