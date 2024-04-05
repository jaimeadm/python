import boto3

sessao = boto3.Session(profile_name="k3s-user", region_name="us-east-1")
client_s3 = sessao.client('s3')

nome_bucket = 'curso-lambda-jaimeadm'

# Primeiro
client_s3.download_file(
    nome_bucket,
    'imagens/logo.png',
    'arquivos/novo_logo.png'
)

# Segundo
arquivo = open('arquivos/foto2.png', 'wb')
client_s3.download_fileobj(
    nome_bucket,
    'imagens/logo.png',
    arquivo
)
arquivo.close()

# Terceiro
planilha_3 = client_s3.get_object(
    Bucket=nome_bucket,
    Key='planilha.xls'
)
planilha_body = planilha_3['Body']
planilha = planilha_body.read()
print(type(planilha))
print(planilha)
print(planilha.decode('utf8'))
