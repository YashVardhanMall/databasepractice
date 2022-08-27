from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://yashvardhanmall:mongodb123@cluster0-shard-00-00.vqb60.mongodb.net:27017,cluster0-shard-00-01.vqb60.mongodb.net:27017,cluster0-shard-00-02.vqb60.mongodb.net:27017/?ssl=true&replicaSet=atlas-e489eh-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.trest

database = client['ineuron']
collection = database['user_data']


@app.route('/insert/mongo', methods=['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(("successfully inserted"))

if __name__ == '__main__':
    app.run()