#importing tools
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping

#Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Set Up App Routes
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

#Set up Scraping Routes and Create Button to start scraping
@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_data = scraping.scrape_all()
    mars.update({}, mars_data, upsert=True)
    #return redirect('/', code=302)
    return "Scraping Successful"
    
#Tell Flask to run 
if __name__ == "__main__":
    app.run()