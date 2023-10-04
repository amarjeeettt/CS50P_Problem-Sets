# pip install fpdf2

# Import the FPDF library
from fpdf import FPDF

# Define a custom PDF class 'PDF' that inherits from FPDF
class PDF(FPDF):
    def header(self):
        # Add a header to the PDF
        self.image('shirtificate.png', 10, 65, 190, 190)  # Add an image to the header
        self.set_font('helvetica', 'B', 45)  # Set font, style, and size for the header text
        self.cell(0, 45, 'CS50 Shirtificate', align='C')  # Add centered text to the header
        self.ln(20)  # Move the cursor down by 20 units

    def footer(self):
        # Add a footer to the PDF
        self.set_font('helvetica', 'B', 25)  # Set font, style, and size for the footer text
        self.set_text_color(255, 255, 255)  # Set text color to white
        self.cell(0, 220, f'{name} took CS50', align='C')  # Add centered text to the footer
        self.ln(20)  # Move the cursor down by 20 units

# Check if the script is run as the main program
if __name__ == '__main__':
    name = input('Name: ')  # Prompt the user for their name

    pdf = PDF()  # Create an instance of the custom PDF class
    pdf.add_page()  # Add a page to the PDF
    pdf.output('shirtificate.pdf')  # Save the PDF as 'shirtificate.pdf'
