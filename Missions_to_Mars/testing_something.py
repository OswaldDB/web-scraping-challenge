from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd

url = "https://space-facts.com/mars/"
table_scrape = pd.read_html(url)
mars_df = pd.DataFrame(table_scrape[0])
mars_data = {}
for i in range(mars_df.shape[0]):
    mars_data.update({mars_df.iloc[i,0]:mars_df.iloc[i,1]})


