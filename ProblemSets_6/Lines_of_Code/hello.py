#this is a comment
def main():
    name = input('What\s your name? ')
    print(hello(name))

# a function that returns 'hello, to the user input of name'
def hello(to: str) -> str:
    return f"hello, {to}"