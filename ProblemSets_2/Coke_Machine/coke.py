# Initialize the amount due with an initial value of 50
amount_due: int = 50

# Start a while loop that continues as long as the amount_due is greater than 0
while amount_due > 0:
    # Print the current amount due
    print(f'Amount Due: {amount_due}')
    
    # Prompt the user to insert a coin and store the value in the 'cost' variable
    cost = int(input('Insert Coin: '))
    
    # Check if the inserted coin value is valid (50, 25, 10, or 5)
    if (cost == 50 or cost == 25 or cost == 10 or cost == 5):
        # Subtract the cost of the coin from the amount due
        amount_due -= cost
    
    # Check if the amount due is now less than or equal to 0
    if (amount_due <= 0):
        # If so, print the amount of change owed (absolute value of amount_due)
        print(f'Change Owed: {abs(amount_due)}')
