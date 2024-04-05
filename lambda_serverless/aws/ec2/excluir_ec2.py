import boto3

sessao = boto3.Session(profile_name='alan', region_name='us-east-1')
client_ec2 = sessao.client('ec2')

id_instancia = 'i-0ee96bf4b8ce0e2d0'

client_ec2.terminate_instances(
    InstanceIds=[id_instancia]
)
