from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']
collection = db['your_collection_name']

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/save', methods=['POST'])
def save_data():
    data = request.get_json()
    collection.insert_one(data)
    return jsonify({'message': 'Data saved successfully.'})

if __name__ == '__main__':
    app.run()
