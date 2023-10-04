# Define a dictionary 'menu' with menu items as keys and their prices as values
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize a variable 'total' to keep track of the total cost
total = 0.0

# Start an infinite loop to allow the user to order menu items
while True:
    try:
        # Prompt the user to input a menu item and capitalize it
        item = input('Item: ').title()

        # Check if the entered menu item is in the 'menu' dictionary
        if item in menu:
            # If the item is in the menu, add its price to the total cost
            total += menu[item]

        # Print the current total cost in currency format with two decimal places
        print(f"Total: ${total:.2f}")

    except EOFError:
        # Handle the End of File (EOF) error by printing a newline and breaking out of the loop
        print()
        break
