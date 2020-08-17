#! python3
# custom_seating.py
# Author: Michael Koundouros
"""
Chapter 15 included a practice project to create custom invitations from a list of guests in a plaintext file. As
an additional project, use the pillow module to create images for custom seating cards for your guests. For each of
the guests listed in the guests.txt file from the resources at https://nostarch.com/automatestuff2/, generate an
image file with the guest name and some flowery decoration. A public domain flower image is also available in the
book's resources.

To ensure that each seating card is the same size, add a black rectangle on the edges of the invitation image so that
when the image is printed out, there will be a guideline for cutting. The PNG files that Pillow produces are set to
72 pixels per inch, so a 4×5-inch card would require a 288×360-pixel image.
usage: python custom_seating.py <file>
where <file> is a text file containing a list of names to be printed on the seating cards.
"""


import sys
from PIL import Image, ImageDraw,  ImageFont


def seating_card(guest_name):
    # Function returns image object of seating card for given guest name

    # Define seating card dimensions (pixels)
    card_width = 360
    card_height = 288

    # Card decoration image
    flower_image = Image.open('morning-glory2.jpg')
    flower_width, flower_height = flower_image.size

    # Create seating card
    card = Image.new('RGBA', (card_width, card_height), 'white')

    # Add decoration to top and bottom of card
    card.paste(flower_image, (0, 0))
    card.paste(flower_image, (0, card_height-flower_height))

    # Add border
    draw = ImageDraw.Draw(card)
    draw.rectangle((0, 0, card_width-1, card_height-1), outline='black')

    # Add name
    brushscript = ImageFont.truetype('BRUSHSCI.TTF', 42)
    w, h = draw.textsize(guest_name, font=brushscript)                # Width and height of text
    draw.text(((card_width-w)/2, (card_height-h)/2), guest_name, fill='black', font=brushscript)

    return card


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 1:
        print('usage: python custom_seating.py <file>')
        sys.exit(1)

    # Create seating cards using text file containing list of names
    filename = args[0]
    i = 1
    try:
        with open(filename, 'r') as file:
            for guest in file:
                name = guest.strip('\n')
                seating_card(name).save(f'seating_card_{i}.png')
                print(f"Creating Seating card for: {name} as: seating_card_{i}.png")
                i += 1
        print('Done!')
    except FileNotFoundError:
        print('file not found!')


if __name__ == '__main__':
    main()
