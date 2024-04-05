import json
import boto3

sessao = boto3.Session()
client_s3 = sessao.client('s3')
cliente_ses = sessao.client('ses')


def envio_email(event, context):

    print(event)

    resultado = client_s3.get_object(
        Bucket=event['Records'][0]['s3']['bucket']['name'],
        Key=event['Records'][0]['s3']['object']['key']
    )

    dados = resultado['Body'].readlines()
    dados = dados[1:]
    for dado in dados:
        linha = dado.decode('utf-8')
        linha = linha.strip()
        usuario = linha.split(',')
        print(usuario)
        enviar_email(usuario[0], usuario[1])

    return {
        "statusCode": 200
    }


def enviar_email(nome, email):

    cliente_ses.send_email(
        Source='alan.silva@jaime.com.br',
        Destination={
            'BccAddresses': [],
            'CcAddresses': [],
            'ToAddresses': [
                email
            ]
        },
        Message={
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Mensagem enviada do Lambda Python'
            },
            'Body': {
                'Html': {
                    'Charset': 'UTF-8',
                    'Data': f'Olá, {nome}, seja bem vindo!'
                }
            }
        }
    )