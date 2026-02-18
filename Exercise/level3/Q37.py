'''Use the pypdf library to open a PDF, extract text from each page, and save all extracted text
to a .txt file. Print the total number of pages processed.'''

from pypdf import PdfReader

reader = PdfReader('git.pdf')

text = " "
for page in reader.pages:
     text += page.extract_text() +'\n'

with open('copy.txt','w') as output:
    output.write(text)

print(len(reader.pages))