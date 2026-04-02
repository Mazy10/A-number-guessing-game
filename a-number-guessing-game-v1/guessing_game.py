"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""

import statistics
import random

def start_game():
    print("Welcome to the guessing game!")
    guesses_list = []
    play_again = "y"

    while play_again == "y":

        if guesses_list:
            print(f'The highest score is: {min(guesses_list)}')
        else:
            print("No high score. Can you be the first?")
        winning_number = random.randint(1,50) 
        guesses = 0   
        while True:
            try:
                guess = int(input("What is the correct number? "))
                guesses += 1
                if guess > 50:
                    print("Oops! This number is outside the range. Please try again")                  
                    continue                 
                
                if guess > winning_number:
                    print("It's lower")
                elif guess < winning_number:
                    print("It's higher")
                else:
                    print("Got it")
                    guesses_list.append(guesses)
                    print(f'The number of guesses it took you was: {guesses}')
                    print(f'The mean of the number of attempts was: {statistics.mean(guesses_list)}')
                    print(f'The median of the number of attempts was: {statistics.median(guesses_list)}')
                    print(f'The mode of the number of attempts was: {statistics.mode(guesses_list)}')
                    print(guesses_list)
                    break
            except ValueError:
                print("Please enter a valid number")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            continue
        else:
            print("Thanks for playing! See you again soon :)")
            break

start_game()

