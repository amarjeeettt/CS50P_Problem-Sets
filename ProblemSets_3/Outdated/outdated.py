# Define a list of month names
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]

# Define a function to validate a date (month and day)
def valid_date(month, day):
    # Check if month is between 1 and 12, and day is between 1 and 31
    return bool(0 < int(month) < 13 and 0 < int(day) < 32)

# Define a function to print a date in the yyyy-mm-dd format
def print_date(month, day, year):
    # Format month and day with leading zeros, then print in yyyy-mm-dd format
    print(f"{year}-{int(month):02}-{int(day):02}")

# Start an infinite loop to continuously receive and process date input
while True:
    try:
        # Prompt the user to input a date and remove leading/trailing whitespace
        date = input('Date: ').strip()

        if '/' in date:
            # If the date contains '/', split it into month, day, and year
            month, day, year = date.split('/')
            
            # Check if the date is valid using the valid_date function
            if valid_date(month, day):
                # Print the valid date in yyyy-mm-dd format and exit the loop
                print_date(month, day, year)
                break

        elif ',' in date:
            # If the date contains ',', split it into month, day, and year
            month, day, year = date.split(' ')
            
            # Check if the day contains ',' and remove it if present
            if ',' in day:
                day = day.replace(',', '')

            # Convert the month name to its corresponding numeric value (1-12)
            month = (months.index(month)) + 1
            
            # Check if the date is valid using the valid_date function
            if valid_date(month, day):
                # Print the valid date in yyyy-mm-dd format and exit the loop
                print_date(month, day, year)
                break

    except:
        pass
