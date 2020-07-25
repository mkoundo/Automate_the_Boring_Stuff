"""
Ref: Chapter 10 - Organising Files
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf
or .jpg). Copy these files from whatever location they are in to a new folder.

"""


import os
import shutil
from pathlib import Path


# Define directory where files will be copied from recursively
source = 'tmp1'
# Define directory where files will be copied to:
target = 'target'
# Define list of file extensions to be copied:
source_file_types = ['pdf', 'png']

# Walk through source directory
# for foldername, subfolders, filenames in os.walk(source):
#     print(f'The current folder is: {foldername}')
#     for subfolder in subfolders:
#         print(f'SUBFOLDER of {foldername}: {subfolder}')
#     for filename in filenames:
#         print(f'FILE INSIDE {foldername}: {filename}')

for source_file_type in source_file_types:
    source_file_list = list(Path(source).glob('**/*.' + source_file_type))
    for source_file in source_file_list:
        print(f'Copied: {source_file}')
        shutil.copy(str(source_file), target)
print(f'Target directory: {target}')
