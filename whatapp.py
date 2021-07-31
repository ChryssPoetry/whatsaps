from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

browser = webdriver.Chrome('Downloads/chromedriver')
browser.get('https://web.whatsapp.com')
wait = WebDriverWait(browser, 600)

target = input('who do you want to hack?')
string = input('what message would you want to send?')
file = input('enter the file location')
x_arg = '//span[contains@title, '+ target + ']'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = browser.find_element_by_class_name("_3OvU8")
for i in range(50):
    input_box.send.keys(string + Keys.ENTER)

attachment_section = browser.find_element_by_xpath('//div[@title = "attach"]')
attachment_section.click()

image = browser.find_element_by_xpath('//input[@accept = image/*,video/mp4,video/3gpp,video/quicktime'])
image.send.keys(file)

sleep(4)
send_button = browser.find_element_by_xpath('//div[@class="_165_h _2HL9j"]')
send_button.click()
