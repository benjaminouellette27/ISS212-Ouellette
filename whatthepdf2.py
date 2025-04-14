'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - whatthepdf2.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

# import modules
import PyPDF2

#prompt user for file path
pdf_file_name = input("Enter the PDF file name or path: ")

# try opening the file in read binary mode
try:
    pdfFile = open(pdf_file_name, "rb")

# error handling
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit(1)

# load pdf using PyPDF2
pdfReader = PyPDF2.PdfReader(pdfFile)

# prompt user for page number
page_number = input("Enter page number: ")

# validate page number
page_number = int(page_number)
if page_number < 1 or page_number > len(pdfReader.pages):
    print("Invalid page number. Please enter a valid page number.")
    exit(1)

# access the page
pageObj = pdfReader.pages[page_number - 1]

# extract and print the text from the page
text_pdf = pageObj.extract_text()


print(text_pdf)
