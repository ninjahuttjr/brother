import requests
from bs4 import BeautifulSoup
import datetime
import json
import os
import random

def get_current_datetime():
    """Returns the current date and time"""
    print("Getting current date and time.")
    return datetime.datetime.now().isoformat()

def browse_web(url: str):
    """Fetches the content of a webpage"""
    print(f"Fetching content from {url}.")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for script in soup(["script", "style"]):
        script.extract()  # Remove these two types of tags
    text = soup.get_text()[:10000]  # Limit the content to the first 4000 characters
    print("Fetched content successfully.")
    return text

def search_gif(search_term: str):
    """Searches for a GIF using the GIPHY API"""
    print(f"Searching for GIF: {search_term}.")
    giphy_api_key = os.getenv('GIPHY_API_KEY')
    response = requests.get(f"http://api.giphy.com/v1/gifs/search?q={search_term}&api_key={giphy_api_key}&limit=10")
    data = json.loads(response.text)
    gif = random.choice(data['data'])
    gif_url = gif['images']['original']['url']
    print("Found GIF URL: ", gif_url)
    return gif_url

# which model should I use for this? most cost effective?

