# Scraping Code

from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd

# NASA Mars News

# Scrape the NASA Mars News Site "https://mars.nasa.gov/news/"
# and collect the latest News Title and Paragraph Text.
# Assign the text to variables that you can reference later.

url = 'https://mars.nasa.gov/news/'
response = requests.get(url)

soup = bs(response.text, 'html.parser')

paragraphs_list = []
items = soup.find_all('div', class_="slide")
for i in items:
    paragraphs_list.append(i.div.a.div.div.text.strip())

headlines_list = []
items = soup.find_all('div', class_="content_title")
for i in items:
    headlines_list.append(i.a.text.strip())

# JPL Mars Space Images - Featured Image

# Visit the url for JPL Featured Space Image here.
# "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
# Use splinter to navigate the site and find the image url for
# the current Featured Mars Image and assign the url string to a variable called featured_image_url.
# Make sure to find the image url to the full size .jpg image.
# Make sure to save a complete url string for this image.

url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

executable_path = {'executable_path': '..\Chromedriver\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

browser.visit(url)

response = requests.get("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")

soup = bs(response.text, 'html.parser')
pictures = soup.find_all('img', class_="thumb")
temp_list = []
for picture in pictures:
    nugget = picture['src'].split("/")[4]
    code = nugget.split("-")[0]
    temp_list.append(code)

featured_picture = "https://www.jpl.nasa.gov/spaceimages/images/largesize/" + temp_list[0] + "_hires.jpg"

browser.quit()

# Mars Facts

# Visit the Mars Facts webpage here "https://space-facts.com/mars/" and
# use Pandas to scrape the table containing facts about the planet including
# Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.

url = "https://space-facts.com/mars/"
table_scrape = pd.read_html(url)
mars_df = pd.DataFrame(table_scrape[0])
mars_data = {}
for i in range(mars_df.shape[0]):
    mars_data.update({mars_df.iloc[i,0]:mars_df.iloc[i,1]})

# Mars Hemispheres

# Visit the USGS Astrogeology site here
# "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# to obtain high resolution images for each of Mar's hemispheres.
# You will need to click each of the links to the hemispheres
# in order to find the image url to the full resolution image.
# Save both the image url string for the full resolution
# hemisphere image, and the Hemisphere title containing the hemisphere name.
# Use a Python dictionary to store the data using the keys img_url and title.
# Append the dictionary with the image url string and the hemisphere title to a list.
# This list will contain one dictionary for each hemisphere.

url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

response = requests.get(url)

soup = bs(response.text, 'html.parser')

target_url_list = []
links = soup.find_all('div', class_="item")
for k in links:
    url = ("https://astrogeology.usgs.gov" + k.a['href'])
    target_url_list.append(url)

scrape_dict = {}

for url in target_url_list:
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    
    titles = soup.find_all('title')
    for title in titles:
        hemi_title = title.text
        
    images = soup.find_all('a')
    for image in images:
        if image.text == "Sample":
            hemi_img = image['href']
    
    scrape_dict.update({hemi_title:hemi_img})

# Create a function called scrape that will execute all of your scraping code
# from above and return one Python dictionary containing all of the scraped data.

def scrape():
    final_dict = {
        "headlines": headlines_list, 
        "paragraphs": paragraphs_list, 
        "picture": featured_picture, 
        "mars_data": mars_data, 
        "hemispheres": scrape_dict}
    return final_dict
