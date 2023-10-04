# Start an infinite loop to repeatedly prompt the user for input until a valid input is provided
while True:
    try:
        # Prompt the user to input a fraction and store it in the 's' variable
        s = input('Fraction: ')
        
        # Split the input string at the '/' character and convert the two parts to integers (x and y)
        x, y = map(int, s.split('/'))

        # Check if y is not equal to 0 and if x is less than or equal to y
        if y != 0 and x <= y:
            # Calculate the fuel percentage and round it to the nearest integer
            fuel_percent = round((x / y) * 100)
        else:
            # If the denominator is 0 or x is greater than y, continue to the next iteration
            continue

        # Check the calculated fuel percentage and print the appropriate message
        if fuel_percent <= 1:
            print('E')  # If fuel_percent is 1% or less, print 'E' for empty
        elif fuel_percent >= 99:
            print('F')  # If fuel_percent is 99% or more, print 'F' for full
        else:
            print(f'{fuel_percent}%')  # Print the fuel percentage in other cases

        # Exit the loop since a valid input has been processed and the result printed
        break

    except (ValueError, ZeroDivisionError):
        pass
