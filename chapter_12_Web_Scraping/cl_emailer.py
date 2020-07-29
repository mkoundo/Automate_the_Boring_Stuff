#! python3
# cl_emailer.py
# Author: Michael Koundouros
"""
Write a program that takes an email address and string of text on the command line and then, using selenium,
logs in to your email account and sends an email of the string to the provided address. (You might want to set up a
separate email account for this program.) This would be a nice way to add a notification feature to your programs.
The webdriver used in this script is for Chrome and is available at https://chromedriver.chromium.org/downloads
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyinputplus as pyip
import time


def emailer(pwd, email_address, my_message):
    browser = webdriver.Chrome()
    browser.get('https://login.live.com/')

    time.sleep(5)                                                                               # pause to let page load

    user_elem = browser.find_element_by_name('loginfmt')                                           # send email username
    user_elem.send_keys('iQIzBAABCAAdFiEEyoO@outlook.com')
    user_elem.send_keys(Keys.ENTER)

    time.sleep(5)                                                                               # pause to let page load

    pwd_elem = browser.find_element_by_name('passwd')                                              # send email password
    pwd_elem.send_keys(pwd)
    pwd_elem.send_keys(Keys.ENTER)

    browser.get('https://outlook.live.com/mail/0/inbox')

    time.sleep(5)                                                                               # pause to let page load

    new_message = browser.find_element_by_xpath('//*[@id="id__3"]')                        # select button 'New message'
    new_message.click()

    time.sleep(5)                                                                               # pause to let page load
                                                                                                  # insert email address
    address_box = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div['
                                                '1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div['
                                                '1]/div/div/input')
    address_box.send_keys(email_address)

    time.sleep(5)

    my_subject = 'Re:'                                                                                  # insert subject
    subject_box = browser.find_element_by_id('TextField92')
    subject_box.send_keys(my_subject)

                                                                                                        # insert message
    message_box = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div['
                                                '1]/div/div/div/div[1]/div[2]/div[1]')
    message_box.send_keys(my_message)

                                                                                                     # click send button
    send_button = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div['
                                                '1]/div/div/div/div[1]/div[3]/div[2]/div[1]/div/span/button[1]')
    send_button.click()

    return


def main():
    email = pyip.inputEmail('Enter email address: ')
    #passwd = pyip.inputPassword(prompt='Enter account password: ', mask='x')
    passwd = input('Enter account password: ')                                      # run in console
    message = input('Enter email message: \n')

    emailer(passwd, email, message)


if __name__ == '__main__':
    main()
