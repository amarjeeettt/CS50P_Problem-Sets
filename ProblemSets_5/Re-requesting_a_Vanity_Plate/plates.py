# Define the main function
def main():
    # Prompt the user to input a license plate and store it in the 'plate' variable
    plate = input("Plate: ")
    
    # Call the 'is_valid' function with the input plate and print the result
    print(is_valid(plate))

# Define the 'is_valid' function to check the validity of a license plate
def is_valid(s):
    found_number = False  # Flag to track if a digit is found
    first_number = True   # Flag to track if the first character is a digit

    # Check the length, alphanumeric characters, and other conditions
    if len(s) < 2 or len(s) > 6 or not s.isalnum():
        return False

    # Check if the plate starts with a digit (invalid)
    if s[:1].isdigit():
        return False

    # Iterate through each character in the plate
    for c in s:
        if c.isdigit():
            found_number = True  # Set the flag to indicate that a digit is found
            if first_number and c.startswith("0"):
                return False  # If the first character is '0', it's invalid
            first_number = False  # Update the flag after the first digit

        elif c.isalpha():
            # If a letter is encountered after a digit, it's invalid
            if found_number:
                return False

        else:
            return False  # If a non-alphanumeric character is found, it's invalid

    return True  # If all checks pass, the plate is valid

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
