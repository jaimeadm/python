import boto3

sessao = boto3.Session(profile_name='alan', region_name='us-east-1')
client_ec2 = sessao.client('ec2')

nome_chave = "jaimeadm"
vpc_id = "vpc-123b0a74"
subnet_id = "subnet-d0044db5"
ami_id = "ami-080e1f13689e07408"

try:
    resposta_sg = client_ec2.create_security_group(
        Description="Python Boto3 SG",
        GroupName="python-sg",
        VpcId=vpc_id,
    )
    sg_id = resposta_sg['GroupId']

    resposta_ingress = client_ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {
                'FromPort': 22,
                'ToPort': 22,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Acesso SSH'
                    }
                ]
            },
            {
                'FromPort': 80,
                'ToPort': 80,
                'IpProtocol': 'tcp',
                'IpRanges': [
                    {
                        'CidrIp': '0.0.0.0/0',
                        'Description': 'Acesso HTTP'
                    }
                ]
            }
        ]
    )

except Exception as erro:
    print(f"Security Group já existe\n {erro}")
    resposta_groupos = client_ec2.describe_security_groups(
        GroupNames=['python-sg']
    )
    sg_id = resposta_groupos['SecurityGroups'][0]['GroupId']

arquivo_user_data = open('user_data.sh', 'r')
user_data = arquivo_user_data.read()

resposta_ec2 = client_ec2.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 8,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2',
                'Encrypted': False
            }
        }
    ],
    UserData=user_data,
    ImageId=ami_id,
    MaxCount=1,
    MinCount=1,
    InstanceType='t2.micro',
    KeyName=nome_chave,
    Monitoring={
        'Enabled': False
    },
    SecurityGroupIds=[sg_id],
    SubnetId=subnet_id,
    InstanceInitiatedShutdownBehavior='terminate',
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'curso-python'
                },
                {
                    'Key': 'Env',
                    'Value': 'Dev'
                }
            ]
        }
    ]
)

print(resposta_ec2)
