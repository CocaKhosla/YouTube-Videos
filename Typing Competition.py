from selenium import webdriver
from time import sleep

browser = webdriver.Chrome('')        # enter location of Chromedriver

browser.get('https://10fastfingers.com')    # website

sleep(3)

browser.find_element_by_link_text('TYPING COMPETITION').click()    # go to typing competition

sleep(2)

browser.find_element_by_xpath('//a[@href = "/competition/"]').click()

# paste the remaining part of the link of the test i.e the hexadecimal part after competition/

sleep(2)

for index in range(0,250):
    str_index = str(index)    # convert index of word into string
    word = browser.find_element_by_css_selector('span.highlight')    # finds WebElement
    word_input = word.text + ' '     # concatenates the word with the space
    browser.find_element_by_xpath('//input[@type = "text"]').send_keys(word_input)  # enter the word
