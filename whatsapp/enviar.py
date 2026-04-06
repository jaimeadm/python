import json
import requests

# 🔐 Credenciais
ZAPI_INSTANCE_ID = "3E2AB2B3EEFD30CF60E64AAAADA6D328"
ZAPI_TOKEN = "602BD6DBE7A2ADE45B4940D6"
CLIENT_TOKEN = "seu token"

# Endpoint atualizado que funciona em instâncias recentes
URL = f"https://api.z-api.io/instances/3E2AB2B3EEFD30CF60E64AAAADA6D328/token/602BD6DBE7A2ADE45B4940D6/send-text"

NUMEROS = [
    "5511985931436"
]


def lambda_handler(event, context):
    print("🚀 Lambda iniciada")
    print("📥 Evento recebido:", json.dumps(event))

    mensagem = event.get("mensagem", "Mensagem padrão enviada pela AWS Lambda")
    print("✉️ Mensagem a enviar:", mensagem)

    headers = {
        "Client-Token": CLIENT_TOKEN,
        "Content-Type": "application/json"
    }

    resultados = []

    for numero in NUMEROS:
        print(f"📲 Enviando para: {numero}")

        payload = {
            "phone": numero,
            "message": mensagem
        }

        print("📦 Payload:", json.dumps(payload))
        print("🌐 URL:", URL)

        try:
            response = requests.post(URL, json=payload, headers=headers)

            print(f"✅ Status HTTP ({numero}):", response.status_code)
            print(f"📨 Resposta ({numero}):", response.text)

            resultados.append({
                "numero": numero,
                "status_code": response.status_code,
                "resposta": response.text
            })

        except Exception as e:
            print(f"❌ Erro ao enviar para {numero}:", str(e))
            resultados.append({
                "numero": numero,
                "erro": str(e)
            })

    print("🏁 Execução finalizada")

    return {
        "statusCode": 200,
        "body": json.dumps(resultados)
    }


if __name__ == "__main__":
    evento_teste = {
        "mensagem": "Teste final funcionando 🚀"
    }
    lambda_handler(evento_teste, None)
