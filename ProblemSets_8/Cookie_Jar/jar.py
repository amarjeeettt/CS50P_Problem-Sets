# Define a Python class named 'Jar' to simulate a cookie jar
class Jar:
    def __init__(self, capacity=12):
        # Constructor method initializes the cookie jar with a given capacity (default is 12)
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity  # Maximum capacity of the jar
        self._size = 0  # Current number of cookies in the jar

    def __str__(self):
        # Custom string representation of the jar, using emoji to represent cookies
        return "🍪" * self.size

    def deposit(self, n):
        # Method to deposit 'n' cookies into the jar
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError("Cannot deposit more cookies than the jar's capacity")
        self._size += n

    def withdraw(self, n):
        # Method to withdraw 'n' cookies from the jar
        if n > self.size:
            raise ValueError("Cannot withdraw more cookies than available in the jar")
        self._size -= n

    @property
    def capacity(self):
        # Property method to get the maximum capacity of the jar
        return self._capacity

    @property
    def size(self):
        # Property method to get the current number of cookies in the jar
        return self._size

# Define the 'main' function to demonstrate the usage of the 'Jar' class
def main():
    # Create a 'Jar' instance with the default capacity (12)
    jar = Jar()

    # Deposit 10 cookies into the jar
    jar.deposit(10)

    # Withdraw 2 cookies from the jar
    jar.withdraw(2)

    # Print the jar's capacity and current size
    print("Jar Capacity:", jar.capacity)
    print("Jar Size:", jar.size)

# Check if the script is run as the main program
if __name__ == '__main__':
    main()  # Call the 'main' function to demonstrate the usage of the 'Jar' class
