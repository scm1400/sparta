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

@app.route('/codes', methods=['GET'])
def group_api():
    group_receive = request.args.get('group')
    print(group_receive)

    all_groups = list(db.codes.find({'group':group_receive},{'_id':False}))

    print(all_groups[0])

    return jsonify({'all_groups':all_groups})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)