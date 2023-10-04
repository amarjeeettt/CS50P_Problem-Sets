# pip install inflect

# Import the 'inflect' library to handle pluralization and singularization of words
import inflect

# Create an instance of the 'inflect' engine
p = inflect.engine()

# Initialize an empty list to store names
name_list = []

# Start an infinite loop to continuously receive user input for names
while True:
    try:
        # Prompt the user to input a name and add it to the 'name_list'
        name = input('Name: ')
        name_list.append(name)

    except EOFError:
        # Handle the End of File (EOF) error by printing a newline and breaking out of the loop
        print()
        break

# Use the 'p.join' method from the 'inflect' engine to join the names
inflect_name = p.join(name_list)

# Print a farewell message using the joined names
print(f'Adieu, adieu, to {inflect_name}')
