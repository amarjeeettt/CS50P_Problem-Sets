#pip install Pillow

# Import necessary modules: sys for command-line arguments, os for file extension handling, and PIL for image processing
import sys
import os
from PIL import Image, ImageOps

# Define the main function
def main():
    # Check the command-line arguments and place the shirt on the image
    check_args()
    check_file()
    place_shirt()

# Define a function to check the command-line arguments
def check_args():
    # Check if there are too few or too many command-line arguments
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')

# Define a function to check the input and output file extensions
def check_file():
    # List of valid image extensions
    extensions = ['.jpg', '.jpeg', '.png']

    # Split input and output file paths into the base file name and extension
    input_filename, input_extension = os.path.splitext(sys.argv[1])
    output_filename, output_extension = os.path.splitext(sys.argv[2])

    # Check if either the input or output extension is not valid
    if input_extension not in extensions or output_extension not in extensions:
        sys.exit('Invalid input or output file extension')

    # Check if the input and output extensions match
    if input_extension != output_extension:
        sys.exit('Input and output file extensions must be the same')

# Define a function to place the shirt on the image
def place_shirt():
    try:
        # Open the shirt image and the muppet image from the specified paths
        shirt = Image.open('shirt.png')
        muppet = Image.open(sys.argv[1])

        # Resize the muppet image to fit the size of the shirt image
        muppet = ImageOps.fit(muppet, shirt.size)

        # Paste the shirt image on top of the resized muppet image
        muppet.paste(shirt, shirt)

        # Save the resulting image to the specified output path
        muppet.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit('Input image does not exist')

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
