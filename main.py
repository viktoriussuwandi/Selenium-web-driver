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
  print('Webscrapping of URL : https://www.python.org/')
  print(json.dumps(events, indent = 4))

  driver.quit()

def wikipedia_org() :
  from selenium.webdriver.common.by import By
  from selenium.webdriver.common.keys import Keys
  from selenium.webdriver.support.ui import Select

  # Extract Website Data
  driver.get('https://www.wikipedia.org/')
  language_el = driver.find_elements(By.CSS_SELECTOR, 'a.link-box strong')
  amount_el   = driver.find_elements(By.CSS_SELECTOR, 'a.link-box bdi')
  language    = [i.text for i in language_el ]
  amount      = [i.text for i in amount_el ]
  articles    = [ 
                  {'language' : unidecode(language[i]), 'articles' : unidecode(amount[i])}
                  for i in range(len(language)) 
                ]
  print('Webscrapping of URL : https://www.wikipedia.org/')
  print(json.dumps(articles, indent = 4))

  # Search Some Information & select language
  search_bar = driver.find_element(By.ID, "searchInput")
  search_bar.send_keys('Python')
  lang_list = driver.find_element(By.XPATH, "/html/body/div[3]/form/fieldset/div/div[1]/div/select")
  select_lang = Select(lang_list)
  select_lang.select_by_visible_text('English')  
  search_bar.send_keys(Keys.ENTER)
  
  heading  = driver.find_elements(By.CLASS_NAME, 'mw-headline')
  headings = [i.text for i in heading]
  print(headings)
  
  driver.quit()

# python_org()
wikipedia_org()