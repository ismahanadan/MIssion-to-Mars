#!/usr/bin/env python
# coding: utf-8

# # Import Dependencies

# In[6]:


# Dependencies
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
import os


# # Scrape the NASA Mars News Site

# In[7]:


# Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. 

#Url to be scraped

url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'


# In[8]:


#Retrieve page with the requests module

response = requests.get(url)


# In[9]:


#Create BeautifulSoup object 
#parse with 'html.parser'

soup = BeautifulSoup(response.text, 'html.parser')


# In[ ]:


#Examine the results 

print(soup.prettify()) 


# In[ ]:


#Extract title text
title = soup.title.text
print(title)


# In[ ]:


#Assign the text to variables

news_title = "Tricky Terrain: Helping to Assure a Safe Rover Landing – NASA’s Mars Exploration Program"


# In[ ]:


#Print all paragraph texts

paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)


# In[ ]:


#Assign the text to variables
news_p = "Managed by the Mars Exploration Program and the Jet Propulsion Laboratory for NASA’s Science Mission Directorate"



# # Mars Facts

# In[ ]:


#Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
#Url to be scraped

url = 'https://space-facts.com/mars/'


# In[ ]:


#Use Pandas to convert the data to a HTML table string

tables = pd.read_html(url)
tables


# In[ ]:


type(tables)


# In[ ]:


df = tables[0]
df


# In[ ]:


df.to_html('table.html')


# In[ ]:


#Convert df to HTML table string

get_ipython().system('open table.html')


# # Mars Hemispheres

# In[5]:


#High resolution images for each of Mar's hemispheres from nasa.gov and planetary.org
#Click on to find the image url to the full resolution image.
#Create a dictionary to store the data using the keys img_url and title.
#Append the dictionary with the image url string and the hemisphere title to a list. 
#This list will contain one dictionary for each hemisphere.


hemisphere_image_urls = [
    
    {"title": "Valles Marineris Hemisphere", "img_url": "https://mars.nasa.gov/system/resources/detail_files/6453_mars-globe-valles-marineris-enhanced-full2.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://www.jpl.nasa.gov/images/cerberus-hemisphere"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://planetary.s3.amazonaws.com/web/assets/pictures/20140202_schiaparelli_enhanced.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://planetary.s3.amazonaws.com/web/assets/pictures/20140202_syrtis_major_enhanced.jpg"},
]        


# In[ ]:





# In[ ]:




