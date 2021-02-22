#!/usr/bin/env python
# coding: utf-8

# MISSION TO MARS CHALLENGE STARTER CODE
# START HERE WITH "STARTER CODE"

# In[58]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[59]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[60]:


# Set the executable path and initialize the chrome browser in splinter
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path)

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/Users/jimmyjordan/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path)


# Visit the NASA Mars News Site

# In[61]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[62]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[63]:


slide_elem.find("div", class_='content_title')


# In[64]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[65]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[ ]:





# JPL Space Images Featured Image

# In[66]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[67]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[68]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[69]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[70]:


# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# Mars Facts

# In[71]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[72]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[73]:


df.to_html()


# ### Mars Weather
# 

# In[74]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[75]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[76]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[77]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[78]:


hemisphere_image_urls = []

for i in range(4):
    #create empty dictionary
    hemispheres = {}
    browser.find_by_css('a.product-item h3')[i].click()
    element = browser.find_link_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    hemisphere_image_urls.append(hemispheres)
    browser.back()


# In[80]:


# 2. Create a list to hold the images and titles.
#hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

#links = browser.find_by_css("a.product-item h3")
#for item in range(len(links)):
    #hemisphere = {}
    #browser.find_by_css("a.product-item h3")[item].click()
    #sample_element = browser.find_link_by_text("Sample").first
    #hemisphere["img_url"] = sample_element["href"]
    #hemisphere["title"] = browser.find_by_css("h2.title").text
    #hemisphere_image_urls.append(hemisphere)
    #browser.back()


# In[81]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[40]:


browser.quit() 


# In[ ]:




