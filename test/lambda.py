# pip install boto3 pymsteams requests python-dateutil
import json
import requests
import boto3

from datetime import datetime
from dateutil import relativedelta

# from teams import enviar_mensagem_teams
# from telegram import enviar_mensagem_telegram

sessao = boto3.Session()
cliente_ce = sessao.client('ce')


def converter_moeda_br(valor_us):

    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    request = requests.get(url)

    if request:

        dic_request = request.json()
        br_currency = dic_request['USDBRL']['bid']

        valor_br = valor_us * float(br_currency)

        return round(float(valor_br), 2)

    else:

        print("Não foi possível acessar a URL")


def lambda_handler(event, context):

    hoje = datetime.today()
    data_inicial = hoje.strftime('%Y-%m-01')

    mes_seguinte = hoje + relativedelta.relativedelta(months=1)
    data_final = mes_seguinte.strftime('%Y-%m-01')

    resposta = cliente_ce.get_cost_and_usage(
        TimePeriod={
            'Start': data_inicial,
            'End': data_final
        },
        Granularity='MONTHLY',
        Metrics=[
            'UnblendedCost'
        ]
    )

    valor = resposta['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']
    valor = round(float(valor), 2)

    valor_br = converter_moeda_br(valor)
    mensagem = f'O custo atual da AWS é de $ {valor} (R$ {valor_br}).'

    # enviar_mensagem_telegram(mensagem)
    # enviar_mensagem_teams(mensagem)
    print(mensagem)
    return {
        "statusCode": 200,
        'total': mensagem
    }


lambda_handler({}, {})
