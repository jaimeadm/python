"""
SharePoint Uploader - Microsoft Graph API
Classe para upload de arquivos no SharePoint Online
"""

import os
import requests
from msal import ConfidentialClientApplication
from typing import Optional, List, Dict
from pathlib import Path


class SharePointUploader:
    """Gerenciador de upload de arquivos para SharePoint via Microsoft Graph API"""

    def __init__(self, tenant_id: str, client_id: str, client_secret: str, site_url: str):
        """
        Inicializa o uploader do SharePoint

        Args:
            tenant_id: ID do tenant do Azure AD
            client_id: ID da aplicação registrada
            client_secret: Secret da aplicação
            site_url: URL completa do site SharePoint (ex: https://empresa.sharepoint.com/sites/Info)
        """
        self.tenant_id = tenant_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.site_url = site_url

        # Extrair domínio e path do site
        parts = site_url.replace("https://", "").split("/sites/")
        self.domain = parts[0]
        self.site_path = f"/sites/{parts[1]}" if len(parts) > 1 else ""

        self.token = None
        self.site_id = None
        self.drives_cache = None

    def _authenticate(self) -> bool:
        """Autentica e obtém token de acesso"""
        try:
            app = ConfidentialClientApplication(
                self.client_id,
                authority=f"https://login.microsoftonline.com/{self.tenant_id}",
                client_credential=self.client_secret
            )

            result = app.acquire_token_for_client(
                scopes=["https://graph.microsoft.com/.default"])

            if "access_token" in result:
                self.token = result["access_token"]
                return True
            else:
                print(
                    f"❌ Erro na autenticação: {result.get('error_description')}")
                return False

        except Exception as e:
            print(f"❌ Erro ao autenticar: {e}")
            return False

    def _get_headers(self) -> Dict[str, str]:
        """Retorna headers para requisições"""
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _get_site_id(self) -> Optional[str]:
        """Obtém o ID do site SharePoint"""
        if self.site_id:
            return self.site_id

        if not self.token:
            if not self._authenticate():
                return None

        try:
            endpoint = f"https://graph.microsoft.com/v1.0/sites/{self.domain}:{self.site_path}"
            response = requests.get(endpoint, headers=self._get_headers())

            if response.status_code == 200:
                self.site_id = response.json()['id']
                return self.site_id
            else:
                print(
                    f"❌ Erro ao obter site ID: {response.status_code} - {response.text}")
                return None

        except Exception as e:
            print(f"❌ Erro ao buscar site: {e}")
            return None

    def list_libraries(self) -> List[Dict[str, str]]:
        """
        Lista todas as bibliotecas de documentos do site

        Returns:
            Lista de dicionários com 'name' e 'id' de cada biblioteca
        """
        if self.drives_cache:
            return self.drives_cache

        site_id = self._get_site_id()
        if not site_id:
            return []

        try:
            endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives"
            response = requests.get(endpoint, headers=self._get_headers())

            if response.status_code == 200:
                drives = response.json()['value']
                self.drives_cache = [
                    {"name": drive['name'], "id": drive['id']}
                    for drive in drives
                ]
                return self.drives_cache
            else:
                print(f"❌ Erro ao listar bibliotecas: {response.status_code}")
                return []

        except Exception as e:
            print(f"❌ Erro ao listar bibliotecas: {e}")
            return []

    def get_library_id_by_name(self, library_name: str) -> Optional[str]:
        """
        Obtém o ID de uma biblioteca pelo nome

        Args:
            library_name: Nome da biblioteca (ex: "Documentos", "Doc para Aprovação")

        Returns:
            ID da biblioteca ou None se não encontrada
        """
        libraries = self.list_libraries()

        for lib in libraries:
            if lib['name'].lower() == library_name.lower():
                return lib['id']

        print(f"⚠️ Biblioteca '{library_name}' não encontrada")
        print(
            f"📚 Bibliotecas disponíveis: {[lib['name'] for lib in libraries]}")
        return None

    def upload_file(
        self,
        file_path: str,
        library_name: str,
        destination_folder: str = "",
        new_filename: Optional[str] = None
    ) -> Optional[str]:
        """
        Faz upload de um arquivo para o SharePoint

        Args:
            file_path: Caminho local do arquivo
            library_name: Nome da biblioteca de destino
            destination_folder: Pasta de destino dentro da biblioteca (opcional)
            new_filename: Novo nome para o arquivo (opcional, usa o nome original se não fornecido)

        Returns:
            URL do arquivo no SharePoint ou None se falhar
        """
        site_id = self._get_site_id()
        if not site_id:
            return None

        library_id = self.get_library_id_by_name(library_name)
        if not library_id:
            return None

        # Determinar nome do arquivo
        filename = new_filename or Path(file_path).name

        # Construir caminho de destino
        destination_path = f"{destination_folder}/{filename}" if destination_folder else filename
        destination_path = destination_path.lstrip("/")

        try:
            # Ler arquivo
            with open(file_path, "rb") as f:
                file_content = f.read()

            # Determinar content type
            content_type = self._get_content_type(filename)

            # Endpoint de upload
            endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{library_id}/root:/{destination_path}:/content"

            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": content_type
            }

            response = requests.put(
                endpoint, headers=headers, data=file_content)

            if response.status_code in [200, 201]:
                file_data = response.json()
                print(f"✅ Upload concluído: {filename}")
                print(f"   📍 URL: {file_data['webUrl']}")
                return file_data['webUrl']
            else:
                print(f"❌ Erro no upload: {response.status_code}")
                print(f"   {response.text}")
                return None

        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {file_path}")
            return None
        except Exception as e:
            print(f"❌ Erro ao fazer upload: {e}")
            return None

    def upload_folder(
        self,
        folder_path: str,
        library_name: str,
        destination_folder: str = "",
        file_extensions: Optional[List[str]] = None,
        recursive: bool = False
    ) -> Dict[str, any]:
        """
        Faz upload de todos os arquivos de uma pasta para o SharePoint

        Args:
            folder_path: Caminho da pasta local
            library_name: Nome da biblioteca de destino
            destination_folder: Pasta de destino dentro da biblioteca (opcional)
            file_extensions: Lista de extensões permitidas (ex: ['.pdf', '.docx']). None = todas
            recursive: Se True, inclui subpastas

        Returns:
            Dicionário com estatísticas do upload: {
                'total': int,
                'success': int,
                'failed': int,
                'urls': List[str],
                'errors': List[Dict]
            }
        """
        stats = {
            'total': 0,
            'success': 0,
            'failed': 0,
            'urls': [],
            'errors': []
        }

        folder_path_obj = Path(folder_path)

        if not folder_path_obj.exists():
            print(f"❌ Pasta não encontrada: {folder_path}")
            return stats

        if not folder_path_obj.is_dir():
            print(f"❌ O caminho não é uma pasta: {folder_path}")
            return stats

        print(f"\n📂 Processando pasta: {folder_path}")
        print(f"🎯 Destino: {library_name}" +
              (f"/{destination_folder}" if destination_folder else ""))
        print("=" * 60)

        # Obter lista de arquivos
        if recursive:
            files = list(folder_path_obj.rglob("*"))
        else:
            files = list(folder_path_obj.glob("*"))

        # Filtrar apenas arquivos (não diretórios)
        files = [f for f in files if f.is_file()]

        # Filtrar por extensão se especificado
        if file_extensions:
            file_extensions = [ext.lower() if ext.startswith(
                '.') else f'.{ext.lower()}' for ext in file_extensions]
            files = [f for f in files if f.suffix.lower() in file_extensions]

        stats['total'] = len(files)

        if stats['total'] == 0:
            print("⚠️ Nenhum arquivo encontrado para upload")
            return stats

        print(f"📊 Total de arquivos a enviar: {stats['total']}\n")

        # Upload de cada arquivo
        for idx, file in enumerate(files, 1):
            # Calcular caminho relativo se for recursive
            if recursive:
                relative_path = file.relative_to(folder_path_obj).parent
                dest_folder = f"{destination_folder}/{relative_path}" if destination_folder else str(
                    relative_path)
                dest_folder = dest_folder.replace('\\', '/').strip('/')
            else:
                dest_folder = destination_folder

            print(f"[{idx}/{stats['total']}] 📤 {file.name}")

            url = self.upload_file(
                file_path=str(file),
                library_name=library_name,
                destination_folder=dest_folder
            )

            if url:
                stats['success'] += 1
                stats['urls'].append(url)
            else:
                stats['failed'] += 1
                stats['errors'].append({
                    'file': str(file),
                    'error': 'Upload falhou'
                })

            print()  # Linha em branco entre arquivos

        # Resumo final
        print("=" * 60)
        print("📊 RESUMO DO UPLOAD")
        print("=" * 60)
        print(f"✅ Sucesso: {stats['success']}/{stats['total']}")
        print(f"❌ Falhas: {stats['failed']}/{stats['total']}")

        if stats['failed'] > 0:
            print("\n⚠️ Arquivos que falharam:")
            for error in stats['errors']:
                print(f"   - {error['file']}")

        return stats

    def upload_content(
        self,
        content: bytes,
        filename: str,
        library_name: str,
        destination_folder: str = "",
        content_type: str = "application/octet-stream"
    ) -> Optional[str]:
        """
        Faz upload de conteúdo em memória (bytes) para o SharePoint

        Args:
            content: Conteúdo em bytes
            filename: Nome do arquivo
            library_name: Nome da biblioteca de destino
            destination_folder: Pasta de destino dentro da biblioteca (opcional)
            content_type: MIME type do conteúdo

        Returns:
            URL do arquivo no SharePoint ou None se falhar
        """
        site_id = self._get_site_id()
        if not site_id:
            return None

        library_id = self.get_library_id_by_name(library_name)
        if not library_id:
            return None

        destination_path = f"{destination_folder}/{filename}" if destination_folder else filename
        destination_path = destination_path.lstrip("/")

        try:
            endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{library_id}/root:/{destination_path}:/content"

            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": content_type
            }

            response = requests.put(endpoint, headers=headers, data=content)

            if response.status_code in [200, 201]:
                file_data = response.json()
                print(f"✅ Upload concluído: {filename}")
                print(f"   📍 URL: {file_data['webUrl']}")
                return file_data['webUrl']
            else:
                print(f"❌ Erro no upload: {response.status_code}")
                print(f"   {response.text}")
                return None

        except Exception as e:
            print(f"❌ Erro ao fazer upload: {e}")
            return None

    @staticmethod
    def _get_content_type(filename: str) -> str:
        """Determina o content type baseado na extensão do arquivo"""
        extension = Path(filename).suffix.lower()

        content_types = {
            '.pdf': 'application/pdf',
            '.docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            '.xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            '.pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
            '.txt': 'text/plain',
            '.csv': 'text/csv',
            '.json': 'application/json',
            '.xml': 'application/xml',
            '.zip': 'application/zip',
            '.jpg': 'image/jpeg',
            '.jpeg': 'image/jpeg',
            '.png': 'image/png',
            '.gif': 'image/gif'
        }

        return content_types.get(extension, 'application/octet-stream')


# ============================================================
# EXEMPLO DE USO - UPLOAD DE PASTA COMPLETA
# ============================================================

if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()

    # Inicializar uploader
    uploader = SharePointUploader(
        tenant_id=os.getenv('SHAREPOINT_TENANT_ID'),
        client_id=os.getenv('SHAREPOINT_CLIENT_ID'),
        client_secret=os.getenv('SHAREPOINT_CLIENT_SECRET'),
        site_url=os.getenv('SHAREPOINT_SITE_URL')
    )

    # EXEMPLO 1: Upload de todos os arquivos da pasta "arquivos"
    stats = uploader.upload_folder(
        folder_path="arquivos",
        library_name="Documentos"
    )

    # EXEMPLO 2: Upload apenas PDFs
    # stats = uploader.upload_folder(
    #     folder_path="arquivos",
    #     library_name="Documentos",
    #     file_extensions=['.pdf']
    # )

    # EXEMPLO 3: Upload para uma subpasta específica
    # stats = uploader.upload_folder(
    #     folder_path="arquivos",
    #     library_name="Documentos",
    #     destination_folder="2026/Fevereiro"
    # )

    # EXEMPLO 4: Upload recursivo (incluindo subpastas)
    # stats = uploader.upload_folder(
    #     folder_path="arquivos",
    #     library_name="Documentos",
    #     recursive=True
    # )

    # EXEMPLO 5: Upload apenas de documentos Office
    # stats = uploader.upload_folder(
    #     folder_path="arquivos",
    #     library_name="Documentos",
    #     file_extensions=['.pdf', '.docx', '.xlsx', '.pptx']
    # )
