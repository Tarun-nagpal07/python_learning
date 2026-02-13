'''
Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more 
functionalities

pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add
 custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

'''

from pypdf import PdfReader, PdfWriter
import time


class IlovePDF:

    @staticmethod
    def merge(file1, file2):

        if not (file1.endswith(".pdf") and file2.endswith(".pdf")):
            print("Wrong file format")
            return

        merger = PdfWriter()
        merger.append(file1)
        merger.append(file2)

        t = time.strftime("%H-%M-%S")
        output_name = f"{t}_merged.pdf"

        with open(output_name, "wb") as output_file:
            merger.write(output_file)

        print("Successfully merged →", output_name)

    @staticmethod
    def rotate(file):

        if not file.endswith(".pdf"):
            print("Wrong file format")
            return

        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            page.rotate(90)
            writer.add_page(page)

        output_name = f"rotated_{file}"

        with open(output_name, "wb") as output_file:
            writer.write(output_file)

        print("Successfully rotated →", output_name)

    @staticmethod
    def security(file, password):

        if not file.endswith(".pdf"):
            print("Wrong file format")
            return

        reader = PdfReader(file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        output_name = f"encrypted_{file}"

        with open(output_name, "wb") as output_file:
            writer.write(output_file)

        print("Successfully encrypted →", output_name)

    @staticmethod
    def splitting(file, no):

        if not file.endswith(".pdf"):
            print("Wrong file format")
            return

        reader = PdfReader(file)

        for i in range(0, len(reader.pages), no):
            writer = PdfWriter()

            for j in range(i, min(i + no, len(reader.pages))):
                writer.add_page(reader.pages[j])

            output_name = f"pages_{i+1}_to_{min(i+no, len(reader.pages))}.pdf"

            with open(output_name, "wb") as output_file:
                writer.write(output_file)

        print("Done splitting")


# Usage
# IlovePDF.merge("git.pdf", "linux.pdf")
# IlovePDF.splitting('linux.pdf',10)

