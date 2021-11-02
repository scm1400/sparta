import json
from pymongo import MongoClient
import boto3
from urllib import parse
import requests
import jwt


def get_secret():
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name="ap-northeast-2"
    )
    get_secret_value_response = client.get_secret_value(
        SecretId='mongo_secret'
    )
    token = get_secret_value_response['SecretString']
    return eval(token)


def db_ops():
    secrets = get_secret()
    client = MongoClient("mongodb://{0}:{1}@{2}".format(secrets['user'], secrets['password'], secrets['host']))
    return client


def lambda_handler(event, context):

    secrets = get_secret()
    api_key = secrets['API_KEY']

    query = event['queryStringParameters']['query']
    proposer_name = event['queryStringParameters']['proposer']
    condition = event['queryStringParameters']['condition']
    pIndex = event['queryStringParameters']['offset']


    # == 검색조건이 없는 경우 ==#
    if query is None and condition is None:
        data = requests.get(
            f'https://open.assembly.go.kr/portal/openapi/nzmimeepazxkubdpn?Key={api_key}&Type={type}&AGE={age}&pIndex={pIndex}&pSize=10')
    # == 법안명으로 검색 ==#
    elif condition == '법안명':
        url = f'https://open.assembly.go.kr/portal/openapi/nzmimeepazxkubdpn?Key={api_key}&Type={type}&AGE={age}&BILL_NAME={query}&pIndex={pIndex}&pSize=10'
        query = encode_querystring(url)

        data = requests.get('https://open.assembly.go.kr/portal/openapi/nzmimeepazxkubdpn?' + query)
    # == 법안발의 제안자명으로 검색==#
    # http://localhost:5000/api/laws?offset=1&proposer=%EA%B9%80%EA%B4%91%EB%A6%BC&condition=%EC%A0%9C%EC%95%88%EC%9E%90
    elif condition == '제안자':
        url = f'https://open.assembly.go.kr/portal/openapi/nzmimeepazxkubdpn?Key={api_key}&Type={type}&AGE={age}&PROPOSER={proposer_name}&pIndex={pIndex}&pSize=10'
        query = encode_querystring(url)
        data = requests.get('https://open.assembly.go.kr/portal/openapi/nzmimeepazxkubdpn?' + query)
    else:
        data = "nodata"

    data = data.json()
    total_count = data['nzmimeepazxkubdpn'][0]['head'][0]['list_total_count']
    data = data['nzmimeepazxkubdpn'][1]['row']

    response = []
    response.append({'total_count': total_count})
    for d in data:
        names = d['PUBL_PROPOSER']
        names = get_other_proposer(names)
        response.append({
            'id': d['BILL_ID'],
            'title': d['BILL_NAME'],  # 법안제목
            'proposer_name': d['RST_PROPOSER'],  # 대표제안자
            'proposer_names': names,  # 대표제안자 외 제안자
            'date': d['PROPOSE_DT'],  # 발의 날짜
            'url': d['DETAIL_LINK'],  # 상세내용 크롤링 link
            'total_count': total_count
        })

    return {
        "statusCode": 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,GET'
        },
        "body": json.dumps({
            "result": "success",
            "articles": response,
        }),
    }


# 요청 URL에서 문자열 쿼리스트링 인코딩
def encode_querystring(url):
    url = parse.urlparse(url)
    query = parse.parse_qs(url.query)
    query = parse.urlencode(query, doseq=True)

    return query


def get_other_proposer(names):
    names = names.split(',')
    names_len = len(names)
    names = ','.join(names[:10])
    if names_len > 10:
        extra = names_len - 10
        names = names + f' 외 {extra}명'
    return names
