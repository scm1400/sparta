import json
import boto3
import pymysql


def db_ops():
    try:
        connection = pymysql.connect(
            host='database-1.cmgwh8mk1bsu.ap-northeast-2.rds.amazonaws.com',
            user='admin',
            password='skek2693!!',
            db='sparta',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    except pymysql.MySQLError as e:
        print("connection error!!")
        return e

    print("connection ok!!")
    return connection


def lambda_handler(event, context):
    body = json.loads(event['body'])
    conn = db_ops()
    cursor = conn.cursor()
    cursor.execute("insert into board(title, content) value('" + body['title'] + "', '" + body['content'] + "')")
    conn.commit()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "success",
        }),
    }
