import json
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

def python_org() :
  from selenium.webdriver.common.by import By
  
  # Get time and event element from python.org
  driver.get('https://www.python.org/')
  time_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
  event_elements = driver.find_elements(By.CSS_SELECTOR, '.event-widget a')

  # Store the element text
  dates  = [i.text for i in time_elements] 
  names  = [i.text for i in event_elements]
  events = [ {'time' : dates[i], 'name' : names[i]} for i in range(len(dates)) ]

  # print the data stored
  print(json.dumps(events, indent = 4))

  driver.quit()

def wikipedia_org() :
  from selenium.webdriver.common.by import By
  
  driver.get('https://www.wikipedia.org/')
  search_bar = driver.find_element(By.ID, "search-input")
  print(f'Search bar tag name : {search_bar.tag_name}')
  
  language_el = driver.find_elements(By.CSS_SELECTOR, 'a.link-box strong')
  amount_el = driver.find_elements(By.CSS_SELECTOR, 'a.link-box bdi')
  language  = [i.text for i in language_el ]
  amount    = [i.text for i in amount_el ]
  articles  = [ 
               {'language' : unidecode(language[i]), 'articles' : unidecode(amount[i])}
               for i in range(len(language)) 
             ]
  print(json.dumps(articles, indent = 4))
  print(f'Languages : {language}')
  print(f'Article amount : {amount}')
  
  driver.quit()
  
# python_org()
wikipedia_org()