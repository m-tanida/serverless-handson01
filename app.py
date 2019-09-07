from chalice import Chalice, Response
from chalicelib.const import *
import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key
from datetime import datetime

app = Chalice(app_name='serverless-handson01')
table = boto3.resource('dynamodb', region_name=REGION_NAME).Table('serverless-handson01-table')
SUCCESS_CD = "0"
ERROR_CD = "9"

@app.route('/', methods=['GET'], cors=cors_config)
def index():
    return 'test'

@app.route('/test1', methods=['GET'], cors=cors_config)
def test1():
    return 'test1'


#########################################################
## 検索処理
#########################################################
@app.route('/workshop', methods=['GET'], cors=cors_config)
def get_workshop():
    
    #検索パラメータの取得
    request = app.current_request.query_params
    if 'ID' in request:
        id = request['ID']
    
    #検索処理
    if id != '':
        #検索条件が指定されている場合
        queryData = table.query(KeyConditionExpression = Key('ID').eq(request['ID']))
    else:
        #検索条件の指定がない場合
        queryData = table.scan()
    
    #検索データの返却 
    if queryData['Items'] == []:
        return {"result": ERROR_CD, "data": "検索結果が 0件 でした。"}
    return {"result": SUCCESS_CD, "data": queryData['Items']}


#########################################################
## 登録処理
#########################################################
@app.route('/workshop', methods=['PUT'], cors=cors_config)
def put_workshop():
    
    #登録パラメータの取得
    request = app.current_request.json_body
    if request['ID'] == '':
        return {"result": ERROR_CD, "data": "社員番号は必須です。"}
        
    #データ登録処理 
    try:
        table.put_item(
            Item={
            'ID': request['ID'],
            'Name': request['Name']
            },
            ConditionExpression='attribute_not_exists(ID)'
        )
        return {"result": SUCCESS_CD, "data": "登録しました。"}
    except Exception as e:
        return {'result':ERROR_CD, 'data': 'すでに登録されています。'}
