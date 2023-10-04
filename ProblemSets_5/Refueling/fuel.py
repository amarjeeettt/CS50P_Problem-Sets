# Define the main function
def main():
    # Prompt the user to input a fraction and store it in the 'fraction' variable
    fraction = input('Fraction: ')
    
    # Call the 'convert' function to calculate the percentage
    percentage = convert(fraction)

    # Call the 'gauge' function to determine the gauge level and print the result
    print(gauge(percentage))

# Define the 'convert' function to calculate the percentage from a given fraction
def convert(fraction):
    try:
        # Split the fraction into numerator and denominator, convert to integers
        x, y = map(int, fraction.split('/'))
        
        # Calculate the percentage and round it to the nearest integer
        return round((x / y) * 100)

    except ValueError:
        raise ValueError("Invalid input: Not a valid fraction")
    except ZeroDivisionError:
        raise ZeroDivisionError("Invalid input: Division by zero")

# Define the 'gauge' function to determine the gauge level based on a percentage
def gauge(percentage):
    if percentage <= 1:
        return 'E'  # Return 'E' for empty if the percentage is less than or equal to 1
    elif percentage >= 99:
        return 'F'  # Return 'F' for full if the percentage is greater than or equal to 99
    else:
        return f'{percentage}%'  # Return the percentage with a '%' symbol for other cases

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
