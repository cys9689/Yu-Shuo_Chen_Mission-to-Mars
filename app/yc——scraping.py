#!/usr/bin/env python
# coding: utf-8

# Import Splinter and BeautifulSoup;
# Import Flask, Mongo and scarping
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import DateTime as dt



# Set the executable path and initialize the chrome browser in splinter
executable_path={'executable_path':'chromedriver'}
browser=Browser('chrome',**executable_path)


    
    
# #Mars nasa news site
# url = 'https://mars.nasa.gov/news/'
# browser.visit(url)
# # Optional delay for loading the page
# browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# #html parser
# html=browser.html
# news_soup=BeautifulSoup(html,'html.parser')
# slide_elm=news_soup.select_one('ul.item_list li.slide')


# slide_elm.find("div",class_='content_title')
# news_title=slide_elm.find("div",class_='content_title').get_text()
# slide_elm.find("div",class_='content_title').get_text()

# news_p=slide_elm.find('div',class_="article_teaser_body").get_text()

# # ### Featured Images

# # Visit URL
# url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
# browser.visit(url)

# # Find and click the full image button
# full_image_elem = browser.find_by_id('full_image')
# full_image_elem.click()


# # Find the more info button and click that
# browser.is_element_present_by_text('more info', wait_time=1)
# more_info_elem = browser.find_link_by_partial_text('more info')
# more_info_elem.click()


# # Parse the resulting html with soup
# html=browser.html
# img_soup=BeautifulSoup(html,'html.parser')
# img_url_rel=img_soup.select_one('figure.lede a img').get("src")

# # Use the base URL to create an absolute URL
# img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
# #pandas read html
# df=pd.read_html('http://space-facts.com/mars/')[0]
# df.columns=['description','value']
# df.set_index('description',inplace=True)
# df.to_html()
# browser.quit()

def mars_news(browser):

   # Visit the mars nasa news site
   url = 'https://mars.nasa.gov/news/'
   browser.visit(url)
   # Optional delay for loading the page
   browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
   html = browser.html
   news_soup = BeautifulSoup(html, 'html.parser')
   try:
       slide_elem = news_soup.select_one('ul.item_list li.slide')
        # Use the parent element to find the first <a> tag and save it as `news_title`
       news_title = slide_elem.find("div", class_='content_title').get_text()
        # Use the parent element to find the paragraph text
       news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
   except AttributeError:
        return None, None

   return news_title,news_p

def featured_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    html = browser.html
    img_soup = BeautifulSoup(html, 'html.parser')
    try:
   # find the relative image url
        img_url_rel = img_soup.select_one('figure.lede a img').get("src")
    except AttributeError:
        return None
    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
    return img_url
def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('http://space-facts.com/mars/')[0]

    except BaseException:
        return None
    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

def scrape_all():
    raise Exception('Pick the appropriate line of code below (inside Nate\'s scraping.py file, in scraping.py function), based on your computer Mac or PC')
    
    browser=Browser("chrome",executable_path="chromedriver",headless=True)
    news_title,news_paragraph=mars_news(browser)
    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
    }
    return data

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())

    
