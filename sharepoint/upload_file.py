from sharepoint_uploader import SharePointUploader
import os
from dotenv import load_dotenv

load_dotenv()

uploader = SharePointUploader(
    tenant_id=os.getenv('SHAREPOINT_TENANT_ID'),
    client_id=os.getenv('SHAREPOINT_CLIENT_ID'),
    client_secret=os.getenv('SHAREPOINT_CLIENT_SECRET'),
    site_url=os.getenv('SHAREPOINT_SITE_URL')
)

print("=" * 60)
print("📤 UPLOAD DO ARQUIVO documento.pdf")
print("=" * 60)

# Upload do seu PDF
url = uploader.upload_file(
    file_path="documento.pdf",   # ← Seu arquivo
    library_name="Documentos",   # ← Biblioteca onde vai aparecer na imagem
    # ← Raiz da biblioteca (ou "General" se quiser na pasta)
    destination_folder=""
)

if url:
    print(f"\n✅ Arquivo enviado com sucesso!")
    print(f"📍 URL: {url}")
    print("\n💡 Acesse: Info > Documentos no SharePoint")
else:
    print("\n❌ Falha no upload")
    print("⚠️ Verifique se o arquivo 'documento.pdf' existe na mesma pasta do script")
