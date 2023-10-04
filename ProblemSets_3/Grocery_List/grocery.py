# Initialize an empty dictionary to store grocery items and their counts
grocery_list = {}

# Start an infinite loop to continuously receive user input
while True:
    try:
        # Prompt the user to input a grocery item and convert it to uppercase
        grocery_input = input().upper()

        # Check if the input is not empty
        if grocery_input:
            # Add the grocery item to the dictionary and update its count
            # If the item doesn't exist in the dictionary, set its count to 1
            # If it already exists, increment its count by 1
            grocery_list[grocery_input] = grocery_list.get(grocery_input, 0) + 1
        else:
            # If the input is empty, exit the loop
            break

    except EOFError:
        # Handle the End of File (EOF) error by breaking out of the loop
        break

# Iterate through the dictionary, sorted by item name
for item, count in sorted(grocery_list.items()):
    # Print the count and the item name
    print(f"{count} {item}")
