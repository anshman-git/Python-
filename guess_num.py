import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while not guessed:
        try:
            guess = int(input("Take a guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"You got it! The number was {secret_number}.")
                print(f"It took you {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

guess_number()