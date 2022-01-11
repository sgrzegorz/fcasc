from minio import Minio
from minio.error import S3Error

# source https://www.youtube.com/watch?v=gfGGGlusbOM

from minio import Minio
from minio.error import ResponseError

from io import BytesIO

host="localhost:9000"
access_key = "jaseem"
secret_key = "iamminio"

minioClient = Minio(host,access_key=access_key, secret_key=secret_key, secure=False)

text = "my minio content fnioafnsof nfianf"
bucket ="coinbase-bucket"
content = BytesIO(bytes(text,'utf-8'))
key = 'sample.text'
size = content.getbuffer().nbytes

try:
    minioClient.put_object(bucket,key,content,size)
    print('Done')
except ResponseError as err:
    print('error',err)


# client = Minio(
#     "play.min.io",
#     access_key="Q3AM3UQ867SPQQA43P2F",
#     secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
# )
#
#
# def sendtext():
#     # Create a client with the MinIO server playground, its access key
#     # and secret key.
#
#     # Make 'asiatrip' bucket if not exist.
#     found = client.bucket_exists("coinbase-bucket")
#     if not found:
#         client.make_bucket("coinbase-bucket")
#     else:
#         print("Bucket 'coinbase-bucket' already exists")
#
#     # Upload '/home/user/Photos/asiaphotos.zip' as object name
#     # 'asiaphotos-2015.zip' to bucket 'asiatrip'.
#     client.fput_object(
#         "coinbase-bucket", "asiaphotos-2015.zip", "/home/user/Photos/asiaphotos.zip",
#     )
#     print(
#         "'/home/user/Photos/asiaphotos.zip' is successfully uploaded as "
#         "object 'asiaphotos-2015.zip' to bucket 'asiatrip'."
#     )