# Import necessary modules: sys for command-line arguments and csv for CSV file handling
import sys
import csv

# Define the main function
def main():
    # Check the command-line arguments and perform data transformation
    check_args()
    scourgify()

# Define a function to check the command-line arguments
def check_args():
    # Check if there are too few or too many command-line arguments
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    # Check if the first argument is a CSV file (ends with '.csv')
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')

# Define a function to perform data transformation on the CSV file
def scourgify():
    try:
        # Open the input and output CSV files
        file_input = open(sys.argv[1], 'r')
        file_output = open(sys.argv[2], 'w')
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

    # Create a CSV DictReader for reading and CSV DictWriter for writing
    data_read = csv.DictReader(file_input, delimiter=',')
    data_write = csv.DictWriter(file_output, ['first', 'last', 'house'])

    data_write.writeheader()  # Write the header to the output file

    # Iterate through rows in the input CSV, split the name into first and last, and write transformed data
    for row in data_read:
        last, first = row['name'].split(',')
        data_write.writerow({
            "first": first.strip(),  # Strip whitespace from the first name
            "last": last,
            "house": row["house"]
        })

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
