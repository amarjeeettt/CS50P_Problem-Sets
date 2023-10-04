# Define the main function
def main():
    # Prompt the user to input a license plate and store it in the 'plate' variable
    plate = input("Plate: ")
    
    # Check if the entered license plate is valid using the 'is_valid' function
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# Define a function to check if a license plate is valid
def is_valid(s):
    found_number = False  # Flag to track if a number has been found
    first_number = True   # Flag to track if the first character is a number

    # Check the length of the input string and if it contains only alphanumeric characters
    if len(s) < 2 or len(s) > 6 or not s.isalnum():
        return False

    # Check if the first character is a digit (license plates typically start with letters)
    if s[:1].isdigit():
        return False

    # Iterate through each character in the input string
    for c in s:
        if c.isdigit():
            found_number = True  # Set the found_number flag to True when a digit is found
            if first_number and c.startswith("0"):
                return False  # Check for leading zeros in numbers
            first_number = False

        elif c.isalpha():
            if found_number:
                return False  # Check for alternating letters and numbers

        else:
            return False  # If a character is neither a letter nor a digit, return False

    return True  # If all checks pass, return True, indicating a valid license plate

# Call the main function to start the program
if __name__ == "__main__":
    main()
