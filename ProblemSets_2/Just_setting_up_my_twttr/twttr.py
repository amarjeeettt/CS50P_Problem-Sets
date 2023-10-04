# Define a list of vowels (both lowercase and uppercase)
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

# Prompt the user to input a string and store it in the 's' variable
s: str = input('Input: ')

# Initialize an empty string 'result' to store the characters without vowels
result = ''

# Iterate through each character in the input string 's'
for text in s:
    # Check if the current character 'text' is not in the list of vowels
    if text not in vowels:
        # If the character is not a vowel, add it to the 'result' string
        result += text

# Print the resulting string without vowels
print(f'Output: {result}')
