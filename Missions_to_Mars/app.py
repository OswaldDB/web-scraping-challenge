from flask import Flask
from scrape_mars import scrape
import pymongo

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the index"

@app.route("/scrape")
def port_scrape():
    final_dict = scrape()
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.marsDB
    allData = db.allData.find()
    db.allData.insert_one(final_dict)
    return "This is the scrape page"

if __name__ == "__main__":
    app.run(debug=True)
