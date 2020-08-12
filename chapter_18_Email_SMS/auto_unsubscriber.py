#! python3
# auto_unsubscriber.py
# Author: Michael Koundouros
"""
Write a program that scans through your email account, finds all the unsubscribe links in all your emails,
and automatically opens them in a browser. This program will have to log in to your email provider’s IMAP server and
download all of your emails. You can use Beautiful Soup (covered in Chapter 12) to check for any instance where the
word unsubscribe occurs within an HTML link tag.

Once you have a list of these URLs, you can use webbrowser.open() to automatically open all of these links in a browser.
"""


import imapclient
import pyzmail
import bs4
import webbrowser


imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
mypass = input('Password:')
imap_obj.login('jowe.blowe.python.ch18@gmail.com', mypass)

print('Fetching Inbox...')
imap_obj.select_folder('INBOX', readonly=True)
UIDS = imap_obj.search(['ALL'])

# For each email UID, fetch the message, parse the html with bs4, select all <a> tags, then
# for each <a> tag that has 'unsubscribe', open the web browser with the tag href link.
for UID in UIDS:
    raw_message = imap_obj.fetch(UID, ['BODY[]'])
    message = pyzmail.PyzMessage.factory(raw_message[UID][b'BODY[]'])
    print(f'Fetching email with subject: {message.get_subject()}')
    if message.html_part != None:
        html_message = message.html_part.get_payload()
        email_soup = bs4.BeautifulSoup(html_message, 'html.parser')
        for tag in email_soup('a'):
            if tag.get_text() == 'unsubscribe':
                print(f"Opening unsubscribe link: {tag['href']}")
                webbrowser.open(tag['href'], new=2)
print('Done!')
