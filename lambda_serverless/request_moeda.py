import json
import requests


def lambda_handler(event, context):
    url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
    request = requests.get(url)
    us_total = 122.39

    dic_request = request.json()
    br_currency = dic_request['USDBRL']['bid']
    br_total = us_total * float(br_currency)

    #print(br_currency)
    #print(dic_request)
    print(round(br_total, 2))

    return {
        'statusCode': 200,
        'body': json.dumps(dic_request)
    }

lambda_handler({}, {})