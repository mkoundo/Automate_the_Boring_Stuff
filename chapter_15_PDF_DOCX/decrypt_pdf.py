#! python3
# decrypt_pdf.py
# Author: Michael Koundouros
"""
Write a program that finds all encrypted PDFs in a folder (and its subfolders) and creates a decrypted copy of the
PDF using a provided password. If the password is incorrect, the program should print a message to the user and
continue to the next PDF.
usage: python decrypt_pdf.py directory password
"""


import sys
import PyPDF2
from pathlib import Path


def decrypt_pdf(search_dir, password):
    # Function searches for all *_encrypted.pdf files in given dir and decrypts them with given password.

    pdf_list = list(Path(search_dir).glob('**/*_encrypted.pdf'))

    print('Decrypting PDF files...')
    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file, strict=False)
            pdf_writer = PyPDF2.PdfFileWriter()
            try:
                pdf_reader.decrypt(password)
                for page_num in range(pdf_reader.numPages):                 # Copy all pages of pdf file
                    pdf_writer.addPage(pdf_reader.getPage(page_num))
                decrypted_pdf = pdf.parent / f'{pdf.stem[:-10]}.pdf'
                print(decrypted_pdf)

                with open(decrypted_pdf, 'wb') as new_pdf:                  # Write decrypted pdf to new file
                    pdf_writer.write(new_pdf)
            except:
                print(f'Decryption failed in {pdf}')

    return


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 2:
        print('usage: python decrypt_pdf.py directory password')
        sys.exit(1)

    decrypt_pdf(Path(args[0]), args[1])
    print('Done!')


if __name__ == '__main__':
    main()
