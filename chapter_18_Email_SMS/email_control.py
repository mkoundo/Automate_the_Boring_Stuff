#! python3
# email_control.py
# Author: Michael Koundouros
"""
Write a program that checks an email account every 15 minutes for any instructions you email it and executes those
instructions automatically. For example, BitTorrent is a peer-to-peer downloading system. Using free BitTorrent
software such as qBittorrent, you can download large media files on your home computer. If you email the program a (
completely legal, not at all piratical) BitTorrent link, the program will eventually check its email,
find this message, extract the link, and then launch qBittorrent to start downloading the file. This way,
you can have your home computer begin downloads while you’re away, and the (completely legal, not at all piratical)
download can be finished by the time you return home.

Chapter 17 covers how to launch programs on your computer using the subprocess.Popen() function. For example,
the following call would launch the qBittorrent program, along with a torrent file:

qbProcess = subprocess.Popen(['C:\\Program Files (x86)\\qBittorrent\\
qbittorrent.exe', 'shakespeare_complete_works.torrent'])

Of course, you’ll want the program to make sure the emails come from you. In particular, you might want to require
that the emails contain a password, since it is fairly trivial for hackers to fake a “from” address in emails. The
program should delete the emails it finds so that it doesn’t repeat instructions every time it checks the email
account. As an extra feature, have the program email or text you a confirmation every time it executes a command.
Since you won’t be sitting in front of the computer that is running the program, it’s a good idea to use the logging
functions (see Chapter 11) to write a text file log that you can check if errors come up.

qBittorrent (as well as other BitTorrent applications) has a feature where it can quit automatically after the
download completes. Chapter 17 explains how you can determine when a launched application has quit with the wait()
method for Popen objects. The wait() method call will block until qBittorrent has stopped, and then your program can
email or text you a notification that the download has completed.
---
I prefer not to install qbittorent, therefore program uses requests module to download links sent via email.
The file downloaded from the email link is a zip archive which is automatically extracted.
"""


import imapclient
import pyzmail
import bs4
import requests
import time
import ezgmail
import traceback
import subprocess
from pathlib import Path


imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
mypass = input('Password:')
imap_obj.login('jowe.blowe.python.ch18@gmail.com', mypass)

starttime = time.time()

while True:
    print('Fetching Inbox...')
    imap_obj.select_folder('INBOX', readonly=False)
    UIDS = imap_obj.search(['ALL'])

    for UID in UIDS:
        # Fetch each email
        raw_message = imap_obj.fetch(UID, ['BODY[]'])
        message = pyzmail.PyzMessage.factory(raw_message[UID][b'BODY[]'])
        print(f'Fetching email with subject: {message.get_subject()}')

        # Find all emails with special subject
        if message.get_subject() == 're: email downloader':
            if message.html_part is not None:
                html_message = message.html_part.get_payload()
                email_soup = bs4.BeautifulSoup(html_message, 'html.parser')

                # retrieve message using bs4, check password and extract all download links
                if email_soup.select('div')[0].getText().find('pass: swordfish'):
                    for tag in email_soup('a'):
                        url = tag['href']
                        filename = Path(url).name

                        # If errors arise, record them in log file
                        try:
                            print(f"Downloading: {url}")
                            res = requests.get(url)
                            res.raise_for_status()
                            with open(filename, 'wb') as download:
                                for chunk in res.iter_content(100000):
                                    download.write(chunk)
                            print(f'Unzipping file: {filename}')
                            unzip_file = subprocess.Popen(f'C:\\Program Files\\Bandizip\\Bandizip.exe x -y {filename}')
                            unzip_file.wait()
                            print('Sending confirmation email...')
                            ezgmail.send('sekid12041@corsj.net', 'Re: email downloader', f"File Downloaded: {url}")

                        except:
                            print('Writing error log...')
                            error_log = open('error_info.log', 'a+')
                            error_log.write(traceback.format_exc())
                            error_log.close()

            imap_obj.delete_messages(UID)
    print('Done!')

    time.sleep(900.0 - ((time.time() - starttime) % 900.0))             # Program sleeps for 15 minutes and repeats
