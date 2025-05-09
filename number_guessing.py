import random
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

def generate_number():
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)

def choose_the_difficulty():
    difficulty = input("Choose the difficulty. Print 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        print(f"You have {EASY_LEVEL} attempts remaining to guess the number.")
        return EASY_LEVEL
    else:
        print(f"You have {HARD_LEVEL} attempts remaining to guess the number.")
        return HARD_LEVEL

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")

    number = generate_number()
    attempts = choose_the_difficulty()

    i = 1
    while i <= attempts:

        try:
            answer = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if answer != number:
            if answer < number:
                print("Too low")
                if attempts - i != 0:
                    print("Guess again")
                    print(f"You have {attempts-i} attempts remaining to guess the number")
            else:
                print("Too high")
                if attempts-i != 0:
                    print("Guess again")
                    print(f"You have {attempts - i} attempts remaining to guess the number")
            i += 1
        else:
            print(f"You got it! The answer was {number}.")
            return
    print("You've run out of guesses. Refresh the page to run again.")

game()