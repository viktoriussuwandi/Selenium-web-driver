# Selenium Setup 1. Import the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Selenium Setup 2. Configure the options to avoid additional driver file needed
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

def search_element() :
  from selenium.webdriver.common.by import By

  driver.get('https://www.wikipedia.org/')
  
  # Find single element, for example : the search bar
  search_bar = driver.find_element(By.ID, "search-input")
  # search_bar = driver.find_element_by_name('search')
  print(search_bar)
  print(search_bar.tag_name)

  # Find multiple elements, for example : all languages available
  link_elements = driver.find_elements(By.CSS_SELECTOR, 'a.link-box strong')
  languages = [l.text for l in link_elements ]
  print(f'Wikipedia languages : {languages}')
  
  # driver.close()
  driver.quit()

search_element()