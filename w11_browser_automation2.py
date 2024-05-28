from selenium import webdriver

browser=webdriver.Chrome('C:/Users/death/Downloads/SOFTWARE/chromedriver_win32/chromedriver.exe')

browser.get('https:/www.youtube.com')

#elem=browser.find_element_by_link_text('Downloads')

#elem.click()

search=browser.find_element_by_class_name('form-control td-search-input ds-input')

search.send_keys('kpop')