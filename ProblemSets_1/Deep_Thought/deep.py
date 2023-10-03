# Prompt the user to enter their answer to the Great Question of Life, the Universe, and Everything
question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

# Convert the user's input to lowercase and remove any leading/trailing whitespace
question = question.lower().strip()

# Use a match statement to evaluate the user's input and provide a response
match question:
    # Check if the user's input is '42', 'forty-two', or 'forty two'
    case '42' | 'forty-two' | 'forty two':
        # If the input matches one of these values, print 'Yes'
        print('Yes')
    # If the input doesn't match any of the specified cases
    case _:
        # Print 'No' to indicate that the input doesn't match the expected answer
        print('No')
