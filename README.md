# web-scraping-challenge

Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

## Step One: Scrapping 

Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

Created a Jupyter Notebook file called mission_to_mars.ipynb and used this to complete all of  scraping and analysis tasks. The following outlines what was tscrape:

  a. Scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. Assign the text to variables that can be referenced later.
  b. Scraped the table containing facts about the planet including Diameter, Mass, etc.
  c. Used Pandas to convert the data to a HTML table string.
  d. Visited USGS Astrogeology site  to obtain high resolution images for each of Mar's hemispheres.
    - Clicked each of the links to the hemispheres in order to find the image url to the full resolution image.
    - Saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Used a Python dictionary to         store the data using the keys img_url and title.
    - Appended the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


## Step Two: MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


Started by converting the Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.


Next, created a route called /scrape that will import the scrape_mars.py script and call the scrape function.

Stored the return value in Mongo as a Python dictionary.



Created a root route / that will query the Mongo database and pass the mars data into an HTML template to display the data.


Created a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements.


