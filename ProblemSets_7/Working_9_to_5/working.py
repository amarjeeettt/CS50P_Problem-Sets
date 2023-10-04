# Import the 're' module for regular expressions
import re

# Define the main function
def main():
    # Prompt the user for input hours and convert them
    s = input("Hours: ").strip()
    print(convert(s))

# Define a function to convert a time string to a standardized format
def convert_time(time_str):
    # Use a regular expression to extract hours, minutes, and AM/PM information from the time string
    hours, minutes, am_pm = re.match(r'(\d{1,2}):?(\d{2})?\s*([APap][Mm])', time_str, re.IGNORECASE).groups()
    hours = int(hours)
    minutes = int(minutes) if minutes else 0

    # Check for invalid time values
    if minutes > 59 or hours > 12:
        raise ValueError("Invalid time")

    # Adjust hours for PM and AM
    if am_pm.upper() == "PM" and hours < 12:
        hours += 12
    elif am_pm.upper() == "AM" and hours == 12:
        hours = 0

    # Format the time as HH:MM
    return f"{hours:02}:{minutes:02}"

# Define a function to convert a time range string to a standardized format
def convert(s):
    # Check if the input contains "am" or "pm" without spaces
    if re.search(r'\d{1,2}(?::\d{2})?[APap][Mm]', s):
        raise ValueError("Invalid input format")

    # Define a regex pattern that matches the valid input format with spaces
    pattern = (
        r'(\d{1,2}(?::\d{2})?\s*[APap][Mm])\s+to\s+(\d{1,2}(?::\d{2})?\s*[APap][Mm])'
    )

    # Attempt to match the input string to the valid pattern
    time_match = re.match(pattern, s, re.IGNORECASE)

    if not time_match:
        raise ValueError("Invalid input format")
    else:
        # Extract and convert the start and end times
        start_time, end_time = time_match.groups()
        start_time = convert_time(start_time)
        end_time = convert_time(end_time)

        # Return the formatted time range
        return f'{start_time} to {end_time}'

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
