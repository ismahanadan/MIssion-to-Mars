from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)



@app.route("/")
def index():
    scraped_data = mongo.db.scrapes.find_one()
    return render_template("index.html", scraped_data=scraped_data)


@app.route("/scrape")
def scraper():
    scraped_data= mongo.db.scraped_data
    mars_data = scrape_mars.scrape()
    scraped_data.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5008)
