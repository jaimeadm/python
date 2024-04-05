import boto3


sessao = boto3.Session(profile_name='k3s-user', region_name='us-east-1')
client_s3 = sessao.client('s3')

nome_bucket = 'curso-lambda-jaimeadm'

resource_s3 = sessao.resource('s3')
bucket = resource_s3.Bucket(nome_bucket)

# Deletar Bucket
# client_s3.delete_bucket(Bucket=nome_bucket)
bucket.delete()

# Deletar Tudo
# objetos = bucket.objects.all()
# # for obj in objetos:
# #     print(obj)
# response = objetos.delete()
# print(response)

# Deletar Vários Arquivos
# response = bucket.delete_objects(
#     Delete={
#         'Objects': [
#             {
#                 'Key': 'planilha.xls'
#             },
#             {
#                 'Key': 'user-icon.png'
#             }
#         ]
#     }
# )
# print(response)

# Deletar Arquivo
# response = client_s3.delete_object(
#     Bucket=nome_bucket,
#     Key="imagens/logo.png"
# )
# print(response)
