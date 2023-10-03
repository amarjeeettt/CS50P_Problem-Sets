# Prompt the user to enter a greeting and store it in the 'greeting' variable
greeting = input('Greeting: ')

# Convert the user's input to lowercase and remove any leading/trailing whitespace
greeting = greeting.lower().strip()

# Check if the word 'hello' is present in the user's greeting
if 'hello' in greeting:
    # If 'hello' is found in the greeting, print '$0'
    print('$0')
# Check if the first character of the greeting is 'h'
elif greeting[0] == 'h':
    # If the first character is 'h', print '$20'
    print('$20')
# If none of the above conditions are met
else:
    # Print '$100' as a default response
    print('$100')
