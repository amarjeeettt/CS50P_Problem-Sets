# This function converts a dollar amount string to a float.
def dollars_to_float(d):
  """Converts a dollar amount string to a float.
  Args:
    d: A dollar amount string, with or without a dollar sign.
  Returns:
    A float representing the dollar amount.
  """
  return float(d.removeprefix('$'))


# This function converts a percentage string to a float.
def percent_to_float(p):
  """Converts a percentage string to a float.
  Args:
    p: A percentage string, with or without a percent sign.
  Returns:
    A float representing the percentage.
  """
  return float(p.removesuffix('%')) / 100


# This function prints a tip amount for a meal.
def main():
  """Prints a tip amount for a meal."""

  # Get the meal cost and tip percentage from the user.
  dollars = dollars_to_float(input("How much was the meal? "))
  percent = percent_to_float(input("What percentage would you like to tip? "))

  # Calculate the tip amount.
  tip = dollars * percent

  # Print the tip amount.
  print(f"Leave ${tip:.2f}")


# Call the main function to start the program.
main()
