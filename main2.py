import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# response  = requests.get("https://www.billboard.com/charts/hot-100/")

# data = response.text

# soup = BeautifulSoup(data,"html.parser")

# name = soup.select(selector="li h3")
# song_list = [song.getText().strip() for song in name]

# final_song_list = []

# for i in range (0,101):
#     final_song_list.append(song_list[i])

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/")

search_bar = driver.find_element(By.XPATH,value='//*[@id="APjFqb"]')

search_bar.send_keys("aryan")
search_bar.send_keys(Keys.ENTER)

# search_button = driver.find_element(By.XPATH,value='//*[@id="search-icon-legacy"]')
# search_button.click()










