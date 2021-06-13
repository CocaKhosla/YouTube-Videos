from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# open browser
browser = webdriver.Chrome('/Users/rohankhosla/Downloads/chromedriver')

# go to LinkedIn
browser.get('http://linkedin.com')

sleep(1)

# press Sign In
browser.find_element_by_link_text('Sign in').click()

sleep(2)

#Enter username in the brackets
browser.find_element_by_id('username').send_keys()

sleep(1)

#Enter password in the brackets
browser.find_element_by_id('password').send_keys()

sleep(1)

browser.find_element_by_xpath("//button[@type = 'submit']").click()

sleep(10)

# Enter names of people you want to sedn the messafe to
names = []
ctr = 0

for name in names:

    # search for the name
    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(name)

    browser.find_element_by_xpath("//input[@type = 'text']").send_keys(Keys.RETURN)

    sleep(3)

    #press enter
    browser.find_element_by_xpath("//button[text() = 'Message']").click()

    # enter your message
    message = ''

    sleep(1)

    # write the message in the message box
    if ctr == 0:
        browser.find_element_by_xpath("//div[@role = 'textbox']").send_keys(message)
    else:
        browser.find_elements_by_xpath("//div[@role = 'textbox']")[ctr].send_keys(message)

    sleep(1)

    # press send
    if ctr == 0:
        browser.find_element_by_xpath("//button[@type = 'submit']").click()
    else:
        browser.find_elements_by_xpath("//button[@type = 'submit']")[ctr].click()

    ctr = ctr + 1

    sleep(1)

    # clear the search browser of previous names
    browser.find_element_by_xpath("//input[@type = 'text']").clear()
