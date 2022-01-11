from minio import Minio
from minio.error import S3Error

# source https://www.youtube.com/watch?v=gfGGGlusbOM

from io import BytesIO

host="localhost:9000"
access_key = "console"
secret_key = "console123"

minioClient = Minio(host,access_key=access_key, secret_key=secret_key, secure=False)

text = "my minio content fnioafnsof nfianf"
bucket ="coinbase-bucket"
content = BytesIO(bytes(text,'utf-8'))
key = 'sample.text'
size = content.getbuffer().nbytes

try:
    minioClient.put_object(bucket,key,content,size)
    print('Done')
except S3Error as err:
    print('error',err)

