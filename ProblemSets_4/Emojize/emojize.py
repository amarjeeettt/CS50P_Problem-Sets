# pip install emoji

# Import the 'emoji' library, which provides emoji-related functionality
import emoji

# Prompt the user to input a text message and store it in the 's' variable
s = input("Input: ")

# Use the 'emoji.emojize' function to replace emoji codes in the input text with actual emojis
# Set the 'language' parameter to 'en' to specify the English language for emoji conversion
output_message = emoji.emojize(f'Output: {s}', language='en')

# Print the output message with emojis
print(output_message)
