#! python3
# cl_emailer.py
# Author: Michael Koundouros
"""
Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos,
and then downloads all the resulting images. You could write a program that works with any photo site that has a
search feature.
usage: python image_downloader.py <search term> directory
<search term> will be searched for on flickr.com
directory is where the images will be saved.
"""

import sys
import os
import requests
import bs4
from pathlib import Path
import re


def flickr_downloader(dir, term):
    # Function downloads images by searching for search <term>, from flickr.com and save them to <dir>.
    url = 'https://www.flickr.com/'
    search_url = url + 'search/?text=' + term

    if not dir.exists():
        os.makedirs(str(dir))

    res = requests.get(search_url)                                      # download site html
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')                   # convert html into a soup object

    # Find images
    regex = re.compile(r'(url\(//)(\S+)(\))')
    print('Downloading images...')
    for style in soup.find_all('div'):                                  # find all <div> tags in html **
        getstyles = style.get('style')                                  # extract style attributes from div tags **
        if getstyles is not None:
            match = regex.search(getstyles)                             # search for image url in style attribute
            if match is not None:
                image = match.group(2)
                medium_image = re.sub(r'(_\D.jpg)|(.jpg)', '_z.jpg', image)   # replace thumbnail with medium size image
                image_url = 'https://' + medium_image                   # generate URL to image
                print(image_url)
                image_file = Path(dir) / Path(medium_image).name        # generate path to save image
                img = requests.get(image_url)                           # download image
                img.raise_for_status()
                write_image = open(image_file, 'wb')
                for chunk in img.iter_content(100_000):                 # save image to a file
                    write_image.write(chunk)
                write_image.close()
    return

    # ** Notes:
    # See http://www.compjour.org/warmups/govt-text-releases/intro-to-bs4-lxml-parsing-wh-press-briefings/
    # for more info on BeautifulSoup.


def main():
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if len(args) != 2:
        print('usage: python image_downloader.py <search term> directory')
        sys.exit(1)
    else:
        search_term = args[0]
        images_dir = Path(args[1])

    flickr_downloader(images_dir, search_term)
    print('Done!')


if __name__ == '__main__':
    main()
