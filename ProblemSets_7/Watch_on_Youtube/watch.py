# Import the 're' module for regular expressions
import re

# Define the main function
def main():
    # Prompt the user for an HTML input string and parse it
    print(parse(input("HTML: ").strip()))

# Define a function to parse the input HTML and extract the YouTube video ID
def parse(s):
    try:
        # Use regular expressions to search for the YouTube video ID within the HTML
        # The regular expression pattern matches the text between 'embed/' and the next '"'
        url = re.search('(?<=embed\/).*?(?=")', s)

        # Construct and return the YouTube URL with the extracted video ID
        return f'https://youtu.be/{url.group(0)}'
    except Exception:
        return None  # Return None if the video ID extraction fails

# Check if the script is run as the main program
if __name__ == "__main__":
    main()  # Call the main function to start the program
