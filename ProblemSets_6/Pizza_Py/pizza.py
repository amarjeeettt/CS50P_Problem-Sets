# pip install tabulate

# Import necessary modules: sys for command-line arguments, csv for CSV file handling, and tabulate for tabular formatting
import sys
import csv
from tabulate import tabulate

# Define the main function
def main():
    # Check the command-line arguments and tabulate the CSV file
    check_args()
    tabulate_csv()

# Define a function to check the command-line arguments
def check_args():
    # Check if there are too many or too few command-line arguments
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')

    # Check if the provided argument is a CSV file (ends with '.csv')
    if '.csv' not in sys.argv[1]:
        sys.exit('Not a CSV file')

# Define a function to tabulate the CSV file
def tabulate_csv():
    try:
        # Open the specified CSV file and create a CSV DictReader
        with open(sys.argv[1]) as file:
            pizza = csv.DictReader(file)
            
            # Use tabulate to format the CSV data as a table with grid formatting
            print(tabulate(pizza, headers='keys', tablefmt='grid'))
    
    except FileNotFoundError:
        sys.exit('File does not exist')  # Exit if the file is not found

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
