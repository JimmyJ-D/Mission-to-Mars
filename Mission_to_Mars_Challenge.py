#!/usr/bin/env python
# coding: utf-8

# In[18]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[5]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/Users/jimmyjordan/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[7]:


#set up the HTML parser:
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[8]:


slide_elem.find("div", class_='content_title')


# In[9]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[ ]:





# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[ ]:





# #Featured Images

# In[15]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[13]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[14]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[16]:


# Find the relative image url, GET LAST UPDATED IMAGE
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[17]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[ ]:





# In[19]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[20]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df.to_html()


# In[23]:


browser.quit() 


# MISSION TO MARS CHALLENGE STARTER CODE

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd


# In[43]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[44]:


# Set the executable path and initialize the chrome browser in splinter
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path)

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/Users/jimmyjordan/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
browser = Browser('chrome', **executable_path)


# Visit the NASA Mars News Site

# In[45]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[46]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[47]:


slide_elem.find("div", class_='content_title')


# In[48]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[49]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# In[ ]:





# JPL Space Images Featured Image

# In[53]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[54]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[57]:


html = browser.html
img_soup = soup(html, 'html.parser')


# In[58]:


img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[59]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[61]:


# Find the more info button and click that
#browser.is_element_present_by_text('more info', wait_time=1)
#more_info_elem = browser.links.find_by_partial_text('more info')
#more_info_elem.click()


# In[62]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[63]:


# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[64]:


# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# Mars Facts

# In[65]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[66]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[67]:


df.to_html()


# ### Mars Weather
# 

# In[68]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[69]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[70]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[71]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[72]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

links = browser.find_by_css("a.product-item h3")
for item in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css("a.product-item h3")[item].click()
    
    sample_element = browser.find_link_by_text("Sample").first
    hemisphere["img_url"] = sample_element["href"]
    
    hemisphere["title"] = browser.find_by_css("h2.title").text
    
    hemisphere_image_urls.append(hemisphere)
    
    browser.back()


# In[74]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[ ]:




