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
    cnt = request.form['cnt_give']
    idx = db.dbStock.count() + 1

    doc = {
        'idx': idx,
        'title': title_receive,
        'content': content_receive,
        'reg_date': posttime,
        'cnt': int(cnt)
    }

    db.dbStock.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

@app.route('/post/update', methods=['POST'])
def update_post():
    idx_receive = request.form['idx_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    today = datetime.now()
    posttime = today.strftime('%Y.%m.%d %H:%M:%S')

    db.dbStock.update_one({'idx': int(idx_receive)}, {'$set': {'title': title_receive}})
    db.dbStock.update_one({'idx': int(idx_receive)}, {'$set': {'content': content_receive}})
    db.dbStock.update_one({'idx': int(idx_receive)}, {'$set': {'reg_date': posttime}})

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

@app.route('/post/details',methods=['POST'])
def details():
    idx_receive = request.form['idx_give']
    find_post = db.dbStock.find_one({'idx': int(idx_receive)})

    current_cnt = find_post['cnt']
    new_cnt = current_cnt + 1

    db.dbStock.update_one({'idx': int(idx_receive)}, {'$set': {'cnt': new_cnt}})
    return{"title":find_post['title'],"content":find_post['content']}

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
