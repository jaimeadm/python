import boto3

sessao = boto3.Session(profile_name='k3s-user', region_name='us-east-1')

client_s3 = sessao.client('s3')
nome_bucket = "curso-lambda-jaimeadm"

try:
    response = client_s3.create_bucket(
        Bucket=nome_bucket,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-2'
        }
    )
    # print(response)

except Exception as erro:
    print('Bucket já existe')
    print(erro)


# Enviar arquivo para o bucket S3
client_s3.upload_file(
    'arquivos/arrows.png',
    nome_bucket,
    'imagens/logo.png'
)

planilha = """
    Nome\tNota
    Ana\t8
    Mario\t9
    Maria\t7
    Carlos\10
"""

client_s3.put_object(
    Body=planilha,
    Bucket=nome_bucket,
    Key='planilha.xls'
)
