from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import csv

# Downloading imdb top 250 movie's data
url = 'https://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv'

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

reviews = soup.select('div.show-more__control')
list = []

for a in reviews:
    print(a.get_text())
    data = {"comments":a.get_text()}
    list.append(a.get_text())