# Prompt the user to enter an expression, expecting three space-separated values (x, y, z)
x, y, z = input('Expression: ').split()

# Use a match statement to evaluate the value of 'y' (the operator)
match y:
    # Check if 'y' is '+', indicating addition
    case '+':
        # Parse 'x' and 'z' as floats, add them, and print the result
        print(float(x) + float(z))
    # Check if 'y' is '-', indicating subtraction
    case '-':
        # Parse 'x' and 'z' as floats, subtract 'z' from 'x', and print the result
        print(float(x) - float(z))
    # Check if 'y' is '*', indicating multiplication
    case '*':
        # Parse 'x' and 'z' as floats, multiply them, and print the result
        print(float(x) * float(z))
    # Check if 'y' is '/', indicating division
    case '/':
        # Parse 'x' and 'z' as floats, divide 'x' by 'z', and print the result
        print(float(x) / float(z))
