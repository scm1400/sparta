from flask import Flask, render_template, jsonify, request
from datetime import datetime
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/base/codes', methods=['GET'])
def show_list():
    groups = list(db.codes.distinct("group"))
    return jsonify(groups)

@app.route('/codes', methods=['POST'])
def post_api():
    groups = list(db.codes.distinct("group"))
    return jsonify(groups)



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)