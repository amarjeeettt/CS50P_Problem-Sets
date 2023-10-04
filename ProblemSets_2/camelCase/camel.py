# Define the main function
def main():
    # Prompt the user to enter a string in camelCase and store it in 'string_case'
    string_case: str = input('camelCase: ')
    # Call the 'convertCase' function to convert the input and print the result
    print(f'snake_case: {convertCase(string_case)}')

# Define a function to convert camelCase to snake_case
def convertCase(s):
    for i in range(len(s)):
        # Check if the current character is uppercase
        if s[i].isupper():
            # If it's uppercase, insert an underscore before it and convert it to lowercase
            s = s[:i] + "_" + s[i].lower() + s[i + 1:]
    # Return the converted string in snake_case
    return s

# Call the main function to start the program
if __name__ == "__main__":
    main()
