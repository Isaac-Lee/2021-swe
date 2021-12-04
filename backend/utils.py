import boto3
from config import *
from botocore.exceptions import ClientError
from time import localtime,strftime
import logging

from config import AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME

#S3 파일 업로드 및 url 가져오기 
def upload_file(file_path,num):

    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # 파일 가져올 경로 
    file_path=file_path
    # 생성한 bucket 이름 
    bucket = BUCKET_NAME

    upload_time = strftime("%Y_%m_%d_%H:%M:%S", localtime())
    # s3 파일 객체 이름
    object_name = upload_time+'_'+str(num)

    # aws region 
    location = 'ap-northeast-2'
   
    #자격 증명 
    s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
    )

     # Upload the file
    try:
        s3_client.upload_file(file_path, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return None
    image_url = f'https://{BUCKET_NAME}.s3.{location}.amazonaws.com/{object_name}'
    return image_url

