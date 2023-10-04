# Import necessary modules: random for generating random numbers and sys for exiting the program
import random
import sys

# Start an infinite loop to continuously play the guessing game
while True:
    try:
        # Prompt the user to input a level (an integer) and store it in the 'level' variable
        level: int = int(input('Input: '))

        # Generate a random number between 1 and the specified level
        random_num = random.randint(1, level)

        # Check if the level is greater than 0
        if level > 0:
            while True:
                try:
                    # Prompt the user to input a guess (an integer) and store it in the 'guess' variable
                    guess: int = int(input('Guess: '))

                    # Compare the guess with the random number
                    if guess < random_num:
                        print('Too small!')
                    elif guess > random_num:
                        print('Too large!')
                    else:
                        sys.exit('Just right!')  # Exit the program with a message if the guess is correct

                except ValueError:
                    pass  # Handle non-integer input for guesses with a 'ValueError'

    except ValueError:
        pass  # Handle non-integer input for the initial level with a 'ValueError'
