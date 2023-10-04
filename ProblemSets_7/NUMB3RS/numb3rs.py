# Import the 're' module for regular expressions
import re

# Define the main function
def main():
    # Prompt the user for an IPv4 address and validate it
    print(validate(input("IPv4 Address: ").strip()))

# Define a function to validate an IPv4 address
def validate(ip):
    try:
        # Define a regular expression pattern to match a valid IPv4 address
        pattern = r'^\d{1,3}(\.\d{1,3}){3}$'
        match = re.match(pattern, ip)  # Use re.match to match the pattern against the input IP address

        # If there is no match, return False
        if not match:
            return False

        # Split the IP address into its four parts (octets)
        parts = ip.split('.')
        
        # Check each part (octet) to ensure it is a valid number (0-255)
        for part in parts:
            if int(part) > 255:  # Convert the part to an integer and check if it's greater than 255
                return False
    except ValueError:
        return False  # Handle the ValueError that may occur if conversion to integer fails

    # If all checks pass, return True (valid IPv4 address)
    return True

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
