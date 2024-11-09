from random import random

import random
from time import perf_counter

logo = '''
 ██████╗ ██╗   ██╗███████╗███████╗███████╗     ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝     ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗█████╗       ██╔██╗ ██║██║   ██║██╔████╔██║██║  ██║█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║██╔══╝       ██║╚██╗██║██║   ██║██║╚██╔╝██║██║  ██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████╗     ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

                      ██████╗ ███╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
                     ██╔═══██╗████╗  ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
                     ██║   ██║██╔██╗ ██║██╔████╔██║██║  ██║█████╗  ██████╔╝
                     ██║   ██║██║╚██╗██║██║╚██╔╝██║██║  ██║██╔══╝  ██╔══██╗
                     ╚██████╔╝██║ ╚████║██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
                      ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
'''
print(logo)

import random


def set_difficulty():
    level = input("Choose the difficulty: easy or hard: ").lower()
    if level == "hard":
        return 5
    else:
        return 10


def check_answer(guess, number):
    if guess > number:
        print("Your guess is too high.")
    elif guess < number:
        print("Your guess is too low.")
    else:
        print(f"Congrats! You guessed the number {number}!")


print("Welcome to the number guessing game!")
number = random.randint(1, 100)
print("The computer has chosen a number between 1 and 100.")


def continue_game():
    turns = set_difficulty()
    print(f"You have {turns} attempts to guess the number.")
    while turns > 0:
        guess = int(input("Make a guess: "))
        check_answer(guess, number)
        turns -= 1

        if guess == number:
            break
        elif turns == 0:
            print("You've run out of attempts! Game over.")
        else:
            print(f"You have {turns} attempts remaining.")

continue_game()













