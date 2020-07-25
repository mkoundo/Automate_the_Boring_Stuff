"""
Ref: Chapter 10 - Organising Files
Ref: Automate the Boring Stuff with Python, Al Sweigart, 2nd Ed., 2019
Author: Michael Koundouros
        July 2020

It’s not uncommon for a few unneeded but humongous files or folders to take up the bulk of the space on your hard
drive. If you’re trying to free up room on your computer, you’ll get the most bang for your buck by deleting the most
massive of the unwanted files. But first you have to find them.

Write a program that walks through a folder tree and searches for exceptionally large files or folders—say,
ones that have a file size of more than 100MB. (Remember that to get a file’s size, you can use os.path.getsize()
from the os module.) Print these files with their absolute path to the screen.

"""


import os
from pathlib import Path


def directory_size(dir_path, file_dict):
    # Function returns the total directory size inc. all sub-directories
    dir_size = 0
    for (dirpath, dirs, files) in os.walk(dir_path):
        for file in files:
            file_path = Path(dirpath) / file
            dir_size += file_dict[file_path]
    return dir_size


def main():
    directory = Path(r'D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files')
    MB = 1024 * 1024
    max_size = 1 * MB

    # Create file dictionary with keys = file paths, values = file sizes
    file_dict = dict.fromkeys(Path(directory).glob('**/*'), 0)
    for file in file_dict.keys():
        file_dict[file] = os.path.getsize(str(file))

    # Print directories larger than maximum size
    for (dirpath, dirs, files) in os.walk(directory):
        folder_size = directory_size(dirpath, file_dict)
        if folder_size > max_size:
            print(f'DIR: {dirpath} {(folder_size/MB):0.2f} MB')

    # Print files larger than maximum size
    for file in file_dict:
        if file_dict[file] > max_size:
            print(f'FILE: {file} {(file_dict[file]/MB):0.2f} MB')


if __name__ == '__main__':
    main()


"""
Program Output:
DIR: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files 3.29 MB
DIR: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files\target 1.64 MB
DIR: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files\tmp1 1.65 MB
DIR: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files\tmp1\tmp2 1.39 MB
DIR: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files\tmp1\tmp2\tmp4 1.39 MB
FILE: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files\target\zophie.png 1.30 MB
FILE: D:\python\1_tutorials\automate_boring_stuff\chapter_10_Org_Files\tmp1\tmp2\tmp4\zophie.png 1.30 MB
"""