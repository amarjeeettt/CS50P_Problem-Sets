# Define the main function
def main():
    # Prompt the user for a greeting and convert it to lowercase with leading/trailing whitespaces removed
    greeting = input('Greeting: ').lower().strip()
    
    # Call the value function with the user's greeting and print the result
    print(value(greeting))

# Define the value function, which assigns a numerical value to a given greeting
def value(greeting):
    if 'hello' in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
