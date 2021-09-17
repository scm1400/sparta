from flask import Flask, render_template, jsonify, request
from datetime import datetime
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

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

    return jsonify({'all_groups':all_groups})

@app.route('/stock', methods = ['POST'])
def save_info():
    info = request.json
    # print(info['market'])
    stocks = list(db.stocks.find({'sector':info['sector'],'market':info['market'],'tag':info['tag']},{'_id':False}))
    return jsonify(stocks)

@app.route('/api', methods=['POST'])
def saving():
    code_number = request.form['code_give'].zfill(6)
    code_receive = f'https://finance.naver.com/item/main.nhn?code={code_number}'

    print(code_number)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(code_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    price = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)').text
    total = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(4) > td:nth-child(2)').text.strip().split()[0]
    per = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(14) > td:nth-child(2)').text.strip()

    print(price, total, per)

    return jsonify({'price': price, 'total':total, 'per':per})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)