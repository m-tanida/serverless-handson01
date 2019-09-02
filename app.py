from chalice import Chalice, Response
from chalicelib.const import *

app = Chalice(app_name='serverless-handson01')

@app.route('/')
def index():
    return 'test'

@app.route('/test1')
def test1():
    return 'test1'