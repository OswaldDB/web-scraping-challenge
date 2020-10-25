from flask import Flask, render_template
from scrape_mars import scrape
import pymongo

app = Flask(__name__)

@app.route("/")
def index():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.marsDB
    allData = db.allData.find()
    for dictionary in allData:
        final_dict = dictionary
    headlines_list = final_dict['headlines']
    paragraphs_list = final_dict['paragraphs']
    picture = final_dict['picture']
    mars_data_dict = final_dict['mars_data']
    hemispheres_dict = final_dict['hemispheres']
    return render_template("index.html", headlines_list = headlines_list, paragraphs_list = paragraphs_list, picture = picture, mars_data_dict = mars_data_dict, hemispheres_dict = hemispheres_dict)

@app.route("/scrape")
def port_scrape():
    final_dict = scrape()
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.marsDB
    allData = db.allData.find()
    db.allData.insert_one(final_dict)
    return str(final_dict)

if __name__ == "__main__":
    app.run(debug=True)
