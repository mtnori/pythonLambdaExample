import os, sys

import boto3
from mypy_boto3_s3 import S3Client

import logging

logger = logging.getLogger()

if __name__ == '__main__':
    s3: S3Client = boto3.client('s3',
                                endpoint_url='http://localhost:9000',
                                aws_access_key_id='admin',
                                aws_secret_access_key='adminpass')
    logger.info('バケット一覧')
    for bucket in s3.list_buckets()['Buckets']:
        print(bucket['Name'])

    logger.info('first.csvの中身')
    obj = s3.get_object(Bucket='sample', Key='first.csv')
    body = obj['Body']
    print(body.read().decode())
