from chalice import CORSConfig
from chalice import Chalice, CognitoUserPoolAuthorizer
from cerberus import Validator
import boto3
from boto3.session import Session
from boto3.dynamodb.conditions import Key
from datetime import datetime, timedelta, timezone
from time import sleep
import os

# 設定値
REGION_NAME='ap-northeast-1'

cors_config = CORSConfig(
    allow_origin='*',
    allow_credentials=True
)
