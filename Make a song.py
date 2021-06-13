from selenium import webdriver
from time import sleep
import random

browser = webdriver.Chrome('/Users/rohankhosla/Downloads/chromedriver')

browser.get('http://sampulator.com')
# go to the website

sleep(5)

browser.find_element_by_xpath("//*[contains(text(), 'keys 1')]").click()
# press the first key or any key you want in order to get the pop up

sleep(2)

browser.find_element_by_xpath("//button[contains(text(), 'Close')]").click()
# close the pop up

sleep(2)

instrument = browser.find_elements_by_class_name('label')
# create a list of all the instruments

for device in instrument:
    print(device.text.lower())

for iteration in range(0,random.randint(5,50)):
    device = instrument[random.randint(0,len(instrument)-1)].text.lower()
    # store the name of each instrument in a variable device

    needed_xpath = '//*[contains(text(), "{}")]'.format(device)
    # create the needed xpath with the variable hence the fancy format

    print(needed_xpath)
    # just for debugging. no use otherwise

    if needed_xpath != '//*[contains(text(), "hat")]' and needed_xpath != '//*[contains(text(), "ha")]':
        # not selecting the other statements cause they were creating errors. idk the reason

        browser.find_element_by_xpath(needed_xpath).click()
        # particular instrument is clicked/played
        sleep(random.random())
