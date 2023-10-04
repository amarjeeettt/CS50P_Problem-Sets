# Define the main function
def main():
    # Prompt the user to input a word and store it in the 'word' variable
    word = input('Input: ')
    
    # Call the 'shorten' function to remove vowels from the input word and print the result
    print(shorten(word))

# Define the 'shorten' function to remove vowels from a given word
def shorten(word):
    result = ''  # Initialize an empty string to store the result
    for text in word:
        # Check if the lowercase version of the character is not a vowel
        if text.lower() not in ['a', 'e', 'i', 'o', 'u']:
            result += text  # Append the character to the result string if it's not a vowel
    return result  # Return the result string without vowels

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
