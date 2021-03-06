from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    scraped_data = {}

   # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 

    #Url to be scraped

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #scrape the table containing facts about the planet including Diameter, Mass, etc.
    #Url to be scraped

    url = 'https://space-facts.com/mars/'

    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    #High resolution images for each of Mar's hemispheres from nasa.gov and planetary.org
    #Click on to find the image url to the full resolution image.
    #Create a dictionary to store the data using the keys img_url and title.
    #Append the dictionary with the image url string and the hemisphere title to a list. 
    #This list will contain one dictionary for each hemisphere.


# hemisphere_image_urls = [
    
#     {"title": "Valles Marineris Hemisphere", "img_url": "https://mars.nasa.gov/system/resources/detail_files/6453_mars-globe-valles-marineris-enhanced-full2.jpg"},
#     {"title": "Cerberus Hemisphere", "img_url": "https://www.jpl.nasa.gov/images/cerberus-hemisphere"},
#     {"title": "Schiaparelli Hemisphere", "img_url": "https://planetary.s3.amazonaws.com/web/assets/pictures/20140202_schiaparelli_enhanced.jpg"},
#     {"title": "Syrtis Major Hemisphere", "img_url": "https://planetary.s3.amazonaws.com/web/assets/pictures/20140202_syrtis_major_enhanced.jpg"},
# ]        





    scraped_data["title"] = soup.find("a", class_="news_title").get_text()
    scraped_data["paragraphs"] = soup.find("span", class_="news_p").get_text()
    scraped_data["facts"] = soup.find("table", class_="tablepress").get_text()

    return scraped_data
