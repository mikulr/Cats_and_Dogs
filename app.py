# our py file to create geojson
import creategeojson
from dotenv import load_dotenv
import os
# modules
from flask import Flask, render_template, redirect, jsonify
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads


# Create an instance of Flask
app = Flask(__name__)

# -------Local Deploy--------
# load_dotenv() # use dotenv to hide sensitive credential as environment variables
# DATABASE_URL=f'mongodb+srv://{os.environ.get("password")}'\
# 	      '@catsdogsandmore.9lyd5hx.mongodb.net/?retryWrites=true&w=majority'# get connection url from environment
# # Use PyMongo to establish Mongo connection
# client = pymongo.MongoClient(DATABASE_URL)


# ---------HEROKU Deploy ---------------
# pull URI from Config Vars
client = pymongo.MongoClient({os.environ.get("MONGODB_URI")})




# create route that renders index.html template
# open on empty page
# @app.route("/")
# def makegeo():
#     # #make the geojson
#     # data = creategeojson.make_geo() 
#     # #Insert the geojson into mongo
#     # mongo_db.geojson.update_one({}, {"$set": data}, upsert=True)
#     # #go to index
#     return redirect('/index')
@app.route("/")
@app.route("/index")
def home():
    
    mapAPI= os.environ.get("mapAPI")
    #pull the geojson from mongo (use find but there is only 1 entry)
    data = client.geojson.collection.find()
    data_list= list(data)

    geojson = {}
    for feature in data_list:
        feature.pop("_id")
        geojson.update(feature)
    # # print(geojson)
   
    #render the page, adding the geojson data from mongo , geojson= geojson 
    return render_template("index.html", geojson = geojson, mapAPI = mapAPI)

@app.route("/charts")
def charts():

   
 # pull the geojson from mongo
    data = client.geojson.collection.find()
    data_list= list(data)

    geojson = {}
    for feature in data_list:
        feature.pop("_id")
        geojson.update(feature)

    #render the page, adding the geojson data from mongo  
    return render_template("charts.html",  geojson= geojson)

   

if __name__ == "__main__":
    app.run(debug=True)  