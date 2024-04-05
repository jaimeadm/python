import boto3

sessao = boto3.Session(
    profile_name='k3s-user',
    region_name='us-east-1'
)

s3_client = sessao.client('s3')
buckets = s3_client.list_buckets()
print(buckets)
