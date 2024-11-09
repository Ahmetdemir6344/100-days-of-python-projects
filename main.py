<<<<<<< HEAD
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
=======
image=("""
  ____                 _                 
 / ___| ___  ___ _ __| |_ ___ _ __ ___  
| |    / _ \/ _ \ '__| __/ _ \ '_ ` _ \ 
| |___|  __/  __/ |  | ||  __/ | | | | |
 \____|\___|\___|_|   \__\___|_| |_| |_|
""")
print(image)
def caeser(original_text, shift_amount, direction):
    output_text = ''
    if direction == 'decode':
        shift_amount = -shift_amount

    for letter in original_text:
        if letter not in alfabet:
            output_text += letter
        else:
            shifted_position = (alfabet.index(letter) + shift_amount) % len(alfabet)
            output_text += alfabet[shifted_position]

    print(f"Your {direction}d result: {output_text}")


should_continue = True
while should_continue:
    alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()  # .lower() burada
    shift = int(input("Type the shift number:\n"))

    caeser(text, shift, direction)

    restart = input("Do you want to try again? (yes or no):\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye")


>>>>>>> 883a2595598a3493a95039b5ce413f86d7a2a1de













