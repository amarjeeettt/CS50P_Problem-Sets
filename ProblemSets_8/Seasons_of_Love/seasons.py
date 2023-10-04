# Import necessary modules
from datetime import date
import inflect, sys, operator

# Initialize the inflect engine for number-to-words conversion
p = inflect.engine()

# Define the main function
def main():
    try:
        # Prompt the user for the date of birth and convert it to age in minutes
        str_date = input('Date of Birth: ')
        print(convert_time(str_date))
    except ValueError:
        sys.exit('Invalid date')

# Define a function to calculate the age in minutes and convert it to words
def convert_time(str_date):
    # Calculate the difference between the current date and the input date of birth
    difference = operator.sub(date.today(), date.fromisoformat(str_date))
    
    # Calculate the age in minutes based on the number of days
    minutes = difference.days * 24 * 60
    
    # Convert the number of minutes to words using the inflect engine
    # The 'andword' parameter is set to an empty string to avoid the word "and" in the output
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
