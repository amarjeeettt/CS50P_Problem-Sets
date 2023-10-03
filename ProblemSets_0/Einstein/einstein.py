# Prompt the user to enter the mass in kilograms.
mass = int(input('m: '))

# Calculate the energy using the mass-energy equivalence equation, E = mc^2.
e = mass * pow(300000000, 2)

# Print the energy to the console.
print('E:', e)