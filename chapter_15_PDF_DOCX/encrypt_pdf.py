#! python3
# encrypt_pdf.py
# Author: Michael Koundouros
"""
Using the os.walk() function from Chapter 10, write a script that will go through every PDF in a folder (and its
subfolders) and encrypt the PDFs using a password provided on the command line. Save each encrypted PDF with an
_encrypted.pdf suffix added to the original filename. Before deleting the original file, have the program attempt to
read and decrypt the file to ensure that it was encrypted correctly.
usage: python encrypt_pdf.py directory password
"""

import os
import sys
import PyPDF2
from pathlib import Path


def encrypt_pdf(search_dir, password):
    # Function searches for all pdf files in given dir and encrypts them with given password.
    # Original pdf files are deleted

    pdf_list = list(Path(search_dir).glob('**/*.pdf'))

    print('Encrypting PDF files...')
    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file, strict=False)       # Read pdf files and suppress warnings
            pdf_writer = PyPDF2.PdfFileWriter()

            for page_num in range(pdf_reader.numPages):                     # Copy all pages of pdf file
                pdf_writer.addPage(pdf_reader.getPage(page_num))

            encrypted_pdf = pdf.parent / f'{pdf.stem}_encrypted.pdf'
            print(encrypted_pdf)
            pdf_writer.encrypt(password)                                    # Encrypt and write pdf to new file
            with open(encrypted_pdf, 'wb') as new_pdf:
                pdf_writer.write(new_pdf)

        print('Verifying encrypted PDFs...')
        with open(encrypted_pdf, 'rb') as verify_pdf:
            pdf_reader = PyPDF2.PdfFileReader(verify_pdf, strict=False)
            try:
                pdf_reader.decrypt(password)
                page_obj = pdf_reader.getPage(0)                            # Check new pdf can be decrypted
                os.remove(pdf)
            except:
                print(f'Encryption failed, {pdf} not deleted')
    return


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 2:
        print('usage: python encrypt_pdf.py directory password')
        sys.exit(1)

    encrypt_pdf(Path(args[0]), args[1])
    print('Done!')


if __name__ == '__main__':
    main()
