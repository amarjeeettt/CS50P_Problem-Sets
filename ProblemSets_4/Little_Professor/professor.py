# Import the 'random' module for generating random numbers
import random

# Define the 'main' function
def main():
    # Initialize the score and tries variables
    score = 0
    tries = 0

    # Get the level from the user
    level = get_level()

    # Loop for 10 rounds of the addition game
    for _ in range(10):
        # Generate two random integers based on the selected level
        x = generate_integer(level)
        y = generate_integer(level)
        solution = x + y

        # Start a loop to handle user input and checking answers
        while True:
            try:
                # Prompt the user for their answer
                user_answer = int(input(f'{x} + {y} = '))
                
                # Check if the user's answer is correct
                if user_answer == solution:
                    error = 0
                    score += 1
                    break
                else:
                    raise ValueError()  # Raise an error if the answer is incorrect
                
            except ValueError:
                tries += 1
                print('EEE')  # Print 'EEE' for an incorrect answer
                
                # Check if the user has exceeded three tries
                if tries >= 3:
                    print(f'{x} + {y} = {solution}')  # Print the correct answer
                    break

    # Print the final score
    print(f'Score {score}')

# Define a function to get the level from the user
def get_level():
    level = 0
    while level <= 0 or level > 3:
        try:
            level = int(input('Level: '))
        except ValueError:
            pass
    return level

# Define a function to generate random integers based on the level
def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the game
