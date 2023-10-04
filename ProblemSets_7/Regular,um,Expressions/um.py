# Import the 're' module for regular expressions
import re
import sys

# Define the main function
def main():
    # Prompt the user for input text and count occurrences of "um" (case-insensitive)
    print(count(input("Text: ").strip()))

# Define a function to count occurrences of "um" (case-insensitive) in a given text
def count(s):
    # Use the re.findall function to find all occurrences of "um" in the input text (case-insensitive)
    # The pattern "\bum\b" matches the word "um" as a whole word (bounded by word boundaries)
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    
    # Return the count of matches (occurrences of "um")
    return len(matches)

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
