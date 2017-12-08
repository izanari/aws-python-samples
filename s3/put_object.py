"""S3へオブジェクトをputするサンプル"""
import boto3

S3_BUCKET_NAME = "hogehoge"

S3_OBJECT_BODY = "hogehoge"
S3_OBJECT_KEY = "sample.txt"

def put_s3object(message, key):
    """s3 へobjectをputする"""
    client = boto3.client('s3')
    print(message)
    response = client.put_object(
        Bucket=S3_BUCKET_NAME,
        Body=message,
        Key=key
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
        print("S3へのput objectが完了しました")
    else:
        print("S3へのput objectが失敗しました")
    return

put_s3object(S3_OBJECT_BODY, S3_OBJECT_KEY)
