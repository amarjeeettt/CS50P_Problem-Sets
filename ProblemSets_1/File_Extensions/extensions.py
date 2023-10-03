# Prompt the user to enter a file name and store it in the 'file' variable
file: str = input('File name: ').lower()

# Check if the file name contains the string '.gif'
if '.gif' in file:
    # If '.gif' is found in the file name, print the corresponding MIME type
    print('image/gif')
# Check if the file name contains the string '.jpg'
elif '.jpg' in file:
    # If '.jpg' is found in the file name, print the corresponding MIME type
    print('image/jpeg')
# Check if the file name contains the string '.jpeg'
elif '.jpeg' in file:
    # If '.jpeg' is found in the file name, print the corresponding MIME type
    print('image/jpeg')
# Check if the file name contains the string '.png'
elif '.png' in file:
    # If '.png' is found in the file name, print the corresponding MIME type
    print('image/png')
# Check if the file name contains the string '.pdf'
elif '.pdf' in file:
    # If '.pdf' is found in the file name, print the corresponding MIME type
    print('application/pdf')
# Check if the file name contains the string '.txt'
elif '.txt' in file:
    # If '.txt' is found in the file name, print the corresponding MIME type
    print('text/plain')
# Check if the file name contains the string '.zip'
elif '.zip' in file:
    # If '.zip' is found in the file name, print the corresponding MIME type
    print('application/zip')
# If none of the above file extensions are found in the file name
else:
    # Print a generic MIME type indicating binary data
    print('application/octet-stream')
