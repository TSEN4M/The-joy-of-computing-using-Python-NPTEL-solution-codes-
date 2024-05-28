# for browser automation we use selenium 

from selenium import webdriver

browser=webdriver.Chrome('C:/Users/death/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe')

browser.get('https:/www.seleniumhq.org')

elem=browser.find_element_by_link_text('Downloads')

elem.click()

target='"Search this site…"'
x_arg='//span[contains(@title,' + target +')]'