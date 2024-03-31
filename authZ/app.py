import base64
import os
from flask import Flask, request, jsonify, redirect
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/authZ')
def authZ():
    # アクセストークンをリクエストヘッダから取得
    access_token = request.headers.get('X-MS-TOKEN-AAD-ACCESS-TOKEN')
    if not access_token:
        return jsonify({"error": "Access token is missing"}), 401

    # Microsoft Graph APIのURL
    url = "https://graph.microsoft.com/v1.0/me/microsoft.graph.checkMemberObjects"

    allow_group_object_id = os.getenv('ALLOW_GROUP_OBJECT_ID', '')
    # ヘッダにアクセストークンを設定
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # APIリクエスト
    response = requests.post(url, headers=headers, json={"ids": [allow_group_object_id]})

    res = response.json()

    value = res.get('value', [])

    if allow_group_object_id in value: return True

    return False
        
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # 環境変数PORTからポート番号を取得。デフォルトは5000番
    app.run(host='0.0.0.0', port=port)