import os
import logging
from aws_lambda_typing import context as context_, events
import boto3
from pathlib import Path
from mypy_boto3_s3 import S3Client
from email.header import Header

BUCKET_NAME = os.environ['BUCKET_NAME']
OBJECT_KEY = os.environ['OBJECT_KEY']
END_POINT_URL = os.getenv('END_POINT_URL')

LOCAL_PATH = Path('/tmp/copy.png')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3: S3Client = boto3.client(
    's3',
    endpoint_url=END_POINT_URL,
    region_name='ap-northeast-1'
)


def handler(event: events.SQSEvent, context: context_.Context) -> None:
    # for record in event['Records']:
    #     print(record['body'])

    s3_object = s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY)

    # S3から取得した内容を取得
    s3_body = s3_object['Body']
    with open(LOCAL_PATH, 'wb') as file:
        # ローカルファイルに書き出す
        for i in s3_body:
            file.write(i)

    # S3に書き出し
    s3.upload_file(Filename=str(LOCAL_PATH),
                   Bucket=BUCKET_NAME,
                   Key='copy.png',
                   ExtraArgs={
                       'Metadata': {
                           'filename': 'copy_image_file.png'
                       }
                   })

    # メタデータの取得方法
    head_obj = s3.head_object(Bucket=BUCKET_NAME, Key='copy.png')
    filename = head_obj['Metadata'].get('filename')

    # Optionalになるので、以下のように取得する
    if filename is not None:
        print(filename)
    else:
        print('filename is None')
