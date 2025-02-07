"""Write a program able to play the "Guess the number" game, where the number to be guessed 
is randomly chosen between 1 and 20."""

import random

def guess_the_number():
    name = input("Hello! What is your name? ")
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    attempts = 0
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break

guess_the_number()

# Example:
# Input: 12 → too low, 16 → too low, 19 → Correct!
