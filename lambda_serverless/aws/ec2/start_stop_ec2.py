import boto3

sessao = boto3.Session(profile_name='alan', region_name='us-east-1')
client_ec2 = sessao.client('ec2')

resposta_instancias = client_ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
                'stopped'
            ]
        },
    ],
)

# print(resposta_instancias)
id_instancia = resposta_instancias['Reservations'][1]['Instances'][0]['InstanceId']

# Desligar EC2
# client_ec2.stop_instances(InstanceIds=[id_instancia])

# Ligar Ec2
client_ec2.start_instances(InstanceIds=[id_instancia])
