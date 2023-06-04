from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb+srv://cgj0079:00791004@cluster0.p6xynpw.mongodb.net/')
db = client['science']
collection = db['name']

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
