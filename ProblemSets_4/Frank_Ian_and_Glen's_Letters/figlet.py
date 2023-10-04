# pip install pyfiglet

# Import necessary modules
import sys
import random
from pyfiglet import Figlet

# Create a Figlet object for text art generation
figlet = Figlet()

# Check the number of command-line arguments (excluding the script name)
if len(sys.argv[1:]) == 0:
    # If no command-line arguments provided, prompt the user for input
    s = input('Input: ')

    # Get the available fonts from Figlet
    font = figlet.getFonts()

    # Select a random font from the available fonts
    random_font = random.choice(font)
    
    # Set the selected font for Figlet
    figlet.setFont(font=random_font)

    # Render and print the input text in the selected font
    print(figlet.renderText(s))

elif len(sys.argv[1:]) == 2:
    # If two command-line arguments are provided
    if sys.argv[1] not in ["-f", "-font"]:
        # Check if the first argument is not '-f' or '-font', and exit with an error message
        sys.exit("Invalid usage")

    # Prompt the user for input
    s = input('Input: ')

    # Get the available fonts from Figlet (this line has no effect, consider removing it)
    figlet.getFonts()
    
    # Set the font for Figlet using the second command-line argument as the font name
    figlet.setFont(font=sys.argv[2])

    # Render and print the input text in the specified font
    print(figlet.renderText(s))

else:
    # If the number of command-line arguments doesn't match the expected cases, exit with an error message
    sys.exit("Invalid usage")
