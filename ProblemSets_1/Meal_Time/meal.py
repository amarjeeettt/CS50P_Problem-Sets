# Define the main function
def main():
    # Prompt the user to enter the time and convert it to lowercase
    time_stamp = input('What time is it? ').lower()

    # Check if the time_stamp contains a space (indicating it includes AM/PM period)
    if ' ' in time_stamp:
        # Split the time and period (AM/PM)
        timeFormat, period = time_stamp.split(' ')
        # Extract the hour and minute from the timeFormat
        hour, minute = map(int, timeFormat.split(':'))
        
        # Adjust the hour based on the AM/PM period
        if 'a.m.' in period and hour == 12:
            hour = 0
        elif 'p.m.' in period and hour != 12:
            hour += 12

        # Check the time and print an appropriate message based on the hour
        if 7 <= hour <= 8:
            print('breakfast time')
        elif 12 <= hour <= 13:
            print('lunch time')
        elif 18 <= hour <= 19:
            print('dinner time')
    
    else:
        # If there's no AM/PM period, convert the time to a 24-hour format
        time = convert(time_stamp)
        # Check the converted time and print an appropriate message
        if 7 <= time <= 8:
            print('breakfast time')
        elif 12 <= time <= 13:
            print('lunch time')
        elif 18 <= time <= 19:
            print('dinner time')

# Define a function to convert time in HH:MM format to a decimal representation
def convert(time):
    hours, minutes = time.split(':')
    # Convert hours and minutes to floating-point numbers
    hours = float(hours) % 24
    minutes = float(minutes) % 60
    minutes = minutes / 60
    # Combine hours and minutes to get the decimal representation of time
    return hours + minutes

# Check if this script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start the program
    main()
