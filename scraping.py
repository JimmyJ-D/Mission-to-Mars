# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/Users/jimmyjordan/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver'}
#browser = Browser('chrome', **executable_path, headless=False)

#Path to chromedriver
#get_ipython().system('which chromedriver')

def scrape_all():
    # Initiate headless driver for deployment
    #browser = Browser("chrome", executable_path="/Users/jimmyjordan/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver", headless=True)
    browser = Browser("chrome", executable_path="chromedriver", headless=True)

    news_title, news_paragraph = mars_news(browser)

    hemisphere_image_urls=hemisphere(browser)
    # Run all scraping functions and store results in dictionary

    data={
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemisphere_image_urls,
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data



#Scrape Mars News
def mars_news(browser):

    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('ul.item_list li.slide')
        #slide_elem.find("div", class_='content_title')

        # Use the parent element to find the first <a> tag and save it as  `news_title`
        news_title = slide_elem.find("div", class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_="article_teaser_body").get_text()

    except AttributeError:
        return None,None #???

    return news_title, news_p


# #Featured Image
def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html' #TA said to change it to this
    browser.visit(url)

    # Find and click the full image button !!!ASK FOR HELP HERE
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Find the more info button and click that !!!ASK FOR HELP HERE
    #browser.is_element_present_by_text('more info', wait_time=1)

    #!!!ASK FOR HELP HERE
    #more_info_elem=browser.links.find_by_partial_text('more info')
    #more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url


#Mars Facts
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

#if __name__ == "__main__":  NOT SURE

    # If running as script, print scraped data
    #print(scrape_all())

#Hemisphere

# Scrape Hemisphere

def hemisphere(browser):
    url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    hemisphere_image_urls = []

    for i in range(4):
        #create empty dictionary
        #hemispheres = {}
        browser.find_by_css('a.product-item h3')[i].click()
        #element = browser.find_link_by_text('Sample').first
        #img_url = element['href']
        #title = browser.find_by_css("h2.title").text
        #hemispheres["img_url"] = img_url
        #hemispheres["title"] = title
        hemisphere_data = scrape_hemisphere(browser.html)
        hemisphere_image_urls.append(hemisphere_data)
        browser.back()
    return hemisphere_image_urls

def scrape_hemisphere(html_text):
    # parse html text
    hemi_soup = soup(html_text, "html.parser")
    # adding try/except for error handling
    try:
        title_elem = hemi_soup.find("h2", class_="title").get_text()
        sample_elem = hemi_soup.find("a", text="Sample").get("href")
    except AttributeError:
        # Image error will return None, for better front-end handling
        title_elem = None
        sample_elem = None
    hemispheres = {
        "title": title_elem,
        "img_url": sample_elem
    }
    return hemispheres


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())
