import boto3

sessao = boto3.Session(profile_name="k3s-user", region_name="us-east-1")

client_s3 = sessao.client('s3')
client_ec2 = sessao.client('ec2')

lista = client_s3.list_buckets()
# print(lista)

recurso_s3 = sessao.resource('s3')
bucket = recurso_s3.Bucket('jmonfiles')
print(bucket)

recurso_ec2 = sessao.resource('ec2')
for instance in recurso_ec2.instances.all():
    print(
        "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\nTags: {6}\n".format(
            instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state, instance.tags
        )
    )
