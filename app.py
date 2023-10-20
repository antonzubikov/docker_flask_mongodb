from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://db:27017')
db = client.mydatabase
collection = db.mycollection


@app.route('/', methods=['GET'])
def get_data():
    data = collection.find_one()
    if data:
        return {
            'message': 'Success',
            'data': data
        }
    else:
        return {
            'message': 'No data found'
        }


@app.route('/', methods=['POST'])
def create_data():
    data = request.json
    collection.insert_one(data)
    return {'message': 'Data created'}


@app.route('/', methods=['PUT'])
def update_data():
    data = request.json
    collection.update_one({}, {'$set': data})
    return {'message': 'Data updated'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
