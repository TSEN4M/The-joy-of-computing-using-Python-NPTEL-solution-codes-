from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"
driver_path = "C:/Users/death/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe"

browser = webdriver.Chrome(options=options, executable_path=driver_path)
browser.get('https://www.youtube.com')

# Finding the search box using its name attribute
search = browser.find_element_by_name('search_query')
search.send_keys('python')
search.submit()  # Submit the form after entering the search query
