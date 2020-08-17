#! python3
# resize_add_logo.py
# Author: Michael Koundouros
"""
Resizes all images in current working directory to fit in a 300x300 square, and adds catlogo.png to the lower-right
corner.

The resizeAndAddLogo.py program in this chapter works with PNG and JPEG files, but Pillow supports many more formats
than just these two. Extend resizeAndAddLogo.py to process GIF and BMP images as well.

Another small issue is that the program modifies PNG and JPEG files only if their file extensions are set in
lowercase. For example, it will process zophie.png but not zophie.PNG. Change the code so that the file extension
check is case insensitive.

Finally, the logo added to the bottom-right corner is meant to be just a small mark, but if the image is about the
same size as the logo itself, the result will look like Figure 19-16. Modify resizeAndAddLogo.py so that the image
must be at least twice the width and height of the logo image before the logo is pasted. Otherwise, it should skip
adding the logo.
"""

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

image_ext = {'.png', '.jpg', '.bmp', '.gif'}

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename[-4:] in str(image_ext) or filename[-4:] in str(image_ext).upper()) \
       or filename == LOGO_FILENAME:
        continue  # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % filename)
        im = im.resize((width, height))

    # Check image is at least twice the width / height of the logo before adding logo
    if width > 2 * logoWidth and height > 2 * logoHeight:
        print('Adding logo to %s...' % filename)
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

        # Save changes.
        im.save(os.path.join('withLogo', filename))
