from flask import Flask, render_template, jsonify, request

from datetime import datetime

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    today = datetime.now()
    posttime = today.strftime('%Y.%m.%d %H:%M:%S')
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    idx = db.dbStock.count() + 1

    doc = {
        'idx': idx,
        'title': title_receive,
        'content': content_receive,
        'reg_date': posttime
    }

    db.dbStock.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})


@app.route('/post', methods=['GET'])
def get_post():
    all_posts = list(db.dbStock.find({}, {'_id': False}))
    return jsonify({'all_posts': all_posts})


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx_receive = request.form['idx_give']
    db.dbStock.delete_one({'idx': int(idx_receive)})
    return {"result": "success"}


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
