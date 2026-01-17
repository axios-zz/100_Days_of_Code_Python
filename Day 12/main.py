import random
from art import logo

EASY_LEVEL_TRY_COUNT = 10
HARD_LEVEL_TRY_COUNT = 5

def defGame(attempts, secret):
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != secret:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > secret:
            print("Too high.")
        elif guess < secret:
            print("Too low.")
        elif guess == secret:
            print(f"You got it! The answer was {secret}")
        else:
            print("Wrong input")
        attempts -= 1

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    attemptsCount = HARD_LEVEL_TRY_COUNT
elif difficulty == "easy":
    attemptsCount = EASY_LEVEL_TRY_COUNT
else:
    print("Wrong input!")

secret_number = random.randint(1,100)
print(secret_number)

defGame(attemptsCount, secret_number)
