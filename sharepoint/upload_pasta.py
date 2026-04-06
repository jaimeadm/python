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
print("📂 UPLOAD DE PASTA COMPLETA")
print("=" * 60)

# Fazer upload de todos os arquivos da pasta "arquivos"
stats = uploader.upload_folder(
    folder_path="arquivos",            # ← Sua pasta
    library_name="Documentos",         # ← Biblioteca destino
    destination_folder=""              # ← Raiz (ou especifique subpasta)
    # file_extensions=['.pdf']         # ← Opcional: filtrar por extensão (ex: ['.pdf', '.docx']
    # recursive=True                   # ← Mantém estrutura de pastas / Incluindo subpastas
)

print(f"\n🎉 Processo finalizado!")
print(f"✅ {stats['success']} arquivos enviados com sucesso")
if stats['failed'] > 0:
    print(f"❌ {stats['failed']} arquivos falharam")
