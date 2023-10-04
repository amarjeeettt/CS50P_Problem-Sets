# pip install validators

# Import the 'validators' library for email validation
import validators

# Define the main function
def main():
    # Prompt the user for an email address and check its validity
    print(is_valid(input("What's your email address? ").strip()))

# Define a function to check the validity of an email address
def is_valid(address: str):
    # Use the 'validators.email' function to check if the provided address is a valid email
    # The function returns True if valid, otherwise False
    return "Valid" if validators.email(address) else "Invalid"

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
