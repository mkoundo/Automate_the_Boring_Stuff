#! python3
# photo_folders.py
# Author: Michael Koundouros
"""
I have a bad habit of transferring files from my digital camera to temporary folders somewhere on the hard drive
and then forgetting about these folders. It would be nice to write a program that could scan the entire hard drive
and find these leftover “photo folders”.

Write a program that goes through every folder on your hard drive and finds potential photo folders. Of course,
first you’ll have to define what you consider a “photo folder” to be; let’s say that it’s any folder where more than
half of the files are photos. And how do you define what files are photos? First, a photo file must have the file
extension .png or .jpg. Also, photos are large images; a photo file’s width and height must both be larger than 500
pixels.
"""


import os
from pathlib import Path
from PIL import Image


root_dir = Path('D:/python/1_tutorials/02_automate_boring_stuff/')
image_ext = {'.png', '.jpg'}

print('Photo folders located at:')

for (dir_path, dirs, files) in os.walk(root_dir):
    num_photo_files = 0
    num_non_photo_files = 0
    for file in files:
        file_path = Path(dir_path) / file
        # print(file_path)
        # Check if file extension isn't .png or .jpg.
        if not file[-4:] in str(image_ext):
            num_non_photo_files += 1
            continue    # skip to next filename

        # Open image file using Pillow.
        im = Image.open(file_path)
        width, height = im.size

        # Check if width & height are larger than 500.
        if width > 500 and height > 100:
            # Image is large enough to be considered a photo.
            num_photo_files += 1
        else:
            # Image is too small to be a photo.
            num_non_photo_files += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    if num_photo_files > num_non_photo_files:
        print(Path(dir_path))

print('Done!')
