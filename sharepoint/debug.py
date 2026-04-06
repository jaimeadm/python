import os
import requests
from msal import ConfidentialClientApplication
from dotenv import load_dotenv

load_dotenv()

# Credenciais
tenant_id = os.getenv('SHAREPOINT_TENANT_ID')
client_id = os.getenv('SHAREPOINT_CLIENT_ID')
client_secret = os.getenv('SHAREPOINT_CLIENT_SECRET')
site_url = os.getenv('SHAREPOINT_SITE_URL')

print("=" * 60)
print("🔐 Autenticando via Microsoft Graph API")
print("=" * 60)
print(f"📍 Tenant ID: {tenant_id}")
print(f"🔑 Client ID: {client_id}")

# Autenticação
app = ConfidentialClientApplication(
    client_id,
    authority=f"https://login.microsoftonline.com/{tenant_id}",
    client_credential=client_secret
)

# Obter token
result = app.acquire_token_for_client(
    scopes=["https://graph.microsoft.com/.default"])

if "access_token" in result:
    print("✅ Token obtido com sucesso!")

    headers = {
        "Authorization": f"Bearer {result['access_token']}",
        "Content-Type": "application/json"
    }

    # Extrair site info da URL
    domain = "jaimeo365.sharepoint.com"
    site_path = "/sites/Info"

    # 1. Obter Site ID
    print("\n📍 Buscando informações do site...")
    site_endpoint = f"https://graph.microsoft.com/v1.0/sites/{domain}:{site_path}"
    response = requests.get(site_endpoint, headers=headers)

    if response.status_code == 200:
        site_data = response.json()
        site_id = site_data['id']
        print(f"✅ Site encontrado: {site_data['displayName']}")
        print(f"   Site ID: {site_id}")
        print(f"   Web URL: {site_data['webUrl']}")

        # 2. Listar Document Libraries (Drives)
        print("\n📁 Listando bibliotecas de documentos...")
        drives_endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
        response = requests.get(drives_endpoint, headers=headers)

        if response.status_code == 200:
            drives = response.json()['value']
            print(f"✅ Encontradas {len(drives)} bibliotecas:")
            for idx, drive in enumerate(drives):
                print(f"   [{idx}] 📚 {drive['name']}")
                print(f"       ID: {drive['id']}")
                print(f"       Tipo: {drive.get('driveType', 'N/A')}")

            # 3. Upload de arquivo para a primeira biblioteca
            if drives:
                drive_id = drives[0]['id']
                drive_name = drives[0]['name']
                print(f"\n📤 Fazendo upload para: {drive_name}")

                # Criar arquivo de teste
                file_name = "teste_upload.txt"
                file_content = "🎉 Teste de upload via Microsoft Graph API\n"
                file_content += f"Data: {__import__('datetime').datetime.now()}\n"
                file_content += f"Biblioteca: {drive_name}\n"

                upload_endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{file_name}:/content"

                upload_response = requests.put(
                    upload_endpoint,
                    headers={
                        "Authorization": f"Bearer {result['access_token']}",
                        "Content-Type": "text/plain"
                    },
                    data=file_content.encode('utf-8')
                )

                if upload_response.status_code in [200, 201]:
                    file_data = upload_response.json()
                    print(f"✅ Arquivo enviado com sucesso!")
                    print(f"   Nome: {file_data['name']}")
                    print(f"   Tamanho: {file_data['size']} bytes")
                    print(f"   URL: {file_data['webUrl']}")
                    print(f"   Criado em: {file_data['createdDateTime']}")

                    # 4. Upload de um PDF de exemplo
                    print(f"\n📄 Testando upload de PDF...")

                    # Criar um PDF simples (ou use um arquivo real)
                    pdf_name = "documento_teste.pdf"

                    # Se você tem um PDF real, use:
                    # with open("seu_arquivo.pdf", "rb") as f:
                    #     pdf_content = f.read()

                    # Para teste, criar conteúdo de exemplo
                    pdf_content = b"%PDF-1.4\nTeste de PDF"

                    pdf_upload_endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{pdf_name}:/content"

                    pdf_response = requests.put(
                        pdf_upload_endpoint,
                        headers={
                            "Authorization": f"Bearer {result['access_token']}",
                            "Content-Type": "application/pdf"
                        },
                        data=pdf_content
                    )

                    if pdf_response.status_code in [200, 201]:
                        pdf_data = pdf_response.json()
                        print(f"✅ PDF enviado com sucesso!")
                        print(f"   Nome: {pdf_data['name']}")
                        print(f"   URL: {pdf_data['webUrl']}")
                    else:
                        print(
                            f"⚠️ Erro no upload do PDF: {pdf_response.status_code}")
                        print(f"   {pdf_response.text}")

                else:
                    print(f"❌ Erro no upload: {upload_response.status_code}")
                    print(f"   {upload_response.text}")
            else:
                print("⚠️ Nenhuma biblioteca encontrada")
        else:
            print(f"❌ Erro ao listar drives: {response.status_code}")
            print(f"   {response.text}")
    else:
        print(f"❌ Erro ao buscar site: {response.status_code}")
        print(f"   Resposta: {response.text}")

        # Diagnóstico adicional
        if response.status_code == 404:
            print("\n🔍 Tentando buscar todos os sites disponíveis...")
            all_sites = requests.get(
                "https://graph.microsoft.com/v1.0/sites?search=*",
                headers=headers
            )
            if all_sites.status_code == 200:
                sites = all_sites.json().get('value', [])
                print(f"✅ Sites encontrados ({len(sites)}):")
                for site in sites[:5]:  # Mostrar só os 5 primeiros
                    print(f"   📌 {site['displayName']}")
                    print(f"      URL: {site['webUrl']}")
else:
    print(f"❌ Erro na autenticação: {result.get('error')}")
    print(f"   Descrição: {result.get('error_description')}")

print("\n" + "=" * 60)
