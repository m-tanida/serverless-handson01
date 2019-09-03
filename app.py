from chalice import Chalice, Response
from chalicelib.const import *
import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key

app = Chalice(app_name='serverless-handson01')
table = boto3.resource('dynamodb', region_name=REGION_NAME).Table('serverless-handson01-table')

@app.route('/')
def index():
    return 'test'

@app.route('/test1')
def test1():
    return 'test1'

@app.route('/get')
def get():
    queryData = table.query(KeyConditionExpression = Key('ID').eq('001'))
    return queryData