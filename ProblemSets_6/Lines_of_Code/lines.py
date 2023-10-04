# Import the 'sys' module for command-line argument handling
import sys

# Define the main function
def main():
    # Check the command-line arguments and the file, then count lines and print the result
    check_args()
    file = check_file()
    print(count_lines(file))
    file.close()

# Define a function to check the command-line arguments
def check_args():
    # Check if there are too many or too few command-line arguments
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    # Check if the provided argument is a Python file (ends with '.py')
    if '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')

# Define a function to check and open the specified file
def check_file():
    try:
        # Attempt to open the file in read mode and return the file object
        file = open(sys.argv[1], 'r')
        return file
    except FileNotFoundError:
        sys.exit('File does not exist')  # Exit if the file is not found

# Define a function to count non-empty lines in the file
def count_lines(file):
    total_lines = 0

    # Iterate through lines in the file
    for line in file.read().splitlines():
        # Skip empty lines
        if len(line.strip()) == 0:
            continue
        # Skip lines that start with "#" (comment lines)
        if not line.strip().startswith("#"):
            total_lines += 1  # Increment the line count for non-empty, non-comment lines

    return total_lines  # Return the total line count

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
