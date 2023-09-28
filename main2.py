import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import googleapiclient.discovery
from google.oauth2 import service_account

response  = requests.get("https://www.billboard.com/charts/hot-100/")

data = response.text

soup = BeautifulSoup(data,"html.parser")

name = soup.select(selector="li h3")
song_list = [song.getText().strip() for song in name]

final_song_list = []

for i in range (0,101):
    final_song_list.append(song_list[i])

# chrome_options = webdriver.ChromeOptions()

# chrome_options.add_experimental_option("detach",True)

# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.youtube.com/")


# search bar correct value 
# search_bar = driver.find_element(By.NAME,value="search_query")

# search_bar.send_keys(f"{song_list[0]} song")
# search_bar.send_keys(Keys.ENTER)

credentials_file = "/Users/aryankumar/Desktop/python/songsdownload-2928ba01d79c.json"

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
credentials = service_account.Credentials.from_service_account_file(credentials_file, scopes=scopes)
youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)


video_url_list = []

for name in final_song_list:
    video_name = name
    search_response = youtube.search().list(
        q=video_name,
        type="video",
        part="id",
        maxResults=1
    ).execute()

    if search_response["items"]:
        video_id = search_response["items"][0]["id"]["videoId"]
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_url_list.append(video_url)
    else:
        print("No video found with that name.")

print(video_url_list)













