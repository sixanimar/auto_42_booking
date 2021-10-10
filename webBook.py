from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome(executable_path='/Users/jguscins/Downloads/chromedriver')

browser.get('https://booking.42wolfsburg.de/')

password = "1a3wob42"
password_put = browser.find_element_by_xpath('//*[@id="pwbox-5"]')
password_put.send_keys(password)

browser.find_element_by_xpath('//*[@id="post-5"]/div[1]/div/form/p[2]/input').click()

time.sleep(1)

category = Select(browser.find_element_by_tag_name('select'))
category.select_by_value('1')

service = Select(browser.find_element_by_tag_name('select'))
category.select_by_value('1')
