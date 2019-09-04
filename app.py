from chalice import Chalice, Response
from chalicelib.const import *
import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key

app = Chalice(app_name='serverless-handson01')
table = boto3.resource('dynamodb', region_name=REGION_NAME).Table('serverless-handson01-table')

@app.route('/', methods=['GET'])
def index():
    return 'test'

@app.route('/test1')
def test1():
    return 'test1'

@app.route('/workshop', methods=['GET'])
def get_workshop():
    request = app.current_request.query_params
    if 'ID' in request:
        queryData = table.query(KeyConditionExpression = Key('ID').eq(request['ID']))
        return queryData['Items']
    else:
        return 'parameter error'

@app.route('/workshop', methods=['PUT'])
def put_workshop():
    request = app.current_request.json_body
    if 'ID' in request:
        queryData = table.query(KeyConditionExpression = Key('ID').eq(request['ID']))
        return queryData['Items']
    else:
        return 'parameter error'