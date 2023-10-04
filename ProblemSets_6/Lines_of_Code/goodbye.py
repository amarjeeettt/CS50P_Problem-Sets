#this is a comment
def main():
    name = input('What\s your name? ')
    print(goodbye(name))

# a function that returns 'goodbye, to the user input of name'
def goodbye(to: str) -> str:
    return f"goodbye, {to}"