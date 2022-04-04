from flask import Flask, render_template, redirect, jsonify, Response
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/michelinStars"
mongo = PyMongo(app)


# @app.route("/")
# def index():  
#     return render_template("index.html")

@app.route("/")
def data_get():
    data_collection = list(mongo.db.oneStars.find({}, {'_id': False}))
    data_collection_2 = list(mongo.db.twoStars.find({}, {'_id': False}))
    data_collection_3 = list(mongo.db.threeStars.find({}, {'_id': False}))
    # all_data_collection = list(mongo.db)
    return render_template('index.html', data_collection=data_collection, data_collection_2=data_collection_2, data_collection_3=data_collection_3)

# @app.route('/get_data')
# def getMyJson():
#     data_collection = mongo.db.students.find_one()
#     data_collection = json.dumps(data_collection)
#     data_collection = {'hey': 'heyyy'}
#     # json = dataFrame.to_json(orient='records', date_format='iso')
#     response = Response(response=json, status=200, mimetype="application/json")
#     return(response)

if __name__ == "__main__":
    app.run(debug=True)
