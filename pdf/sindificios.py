import fitz  # PyMuPDF
import re

# Caminho do PDF
pdf_path = "/mnt/jrenova/sindificios_boletos/sindificios_boletos1.pdf"

# Abrir o PDF
doc = fitz.open(pdf_path)

# Expressão regular atualizada
padrao = re.compile(r"\((\d+)\)(\d{4})\s+(.+?)\s+-\s+CNPJ:\s+(\d{14})")

# Armazenar dados únicos com a página
dados_extraidos = []

for i, page in enumerate(doc, start=1):
    texto = page.get_text()
    match = padrao.search(texto)
    if match:
        _, cod, nome, cnpj = match.groups()
        dados_extraidos.append((cod, nome.strip(), cnpj, i))

# Mostrar resultados
print(f"{'Código':<10} | {'Condomínio':<50} | {'CNPJ':<14} | Página")
print("-" * 100)
for codigo, nome, cnpj, pagina in sorted(dados_extraidos, key=lambda x: x[3]):
    print(f"{codigo:<10} | {nome:<50} | {cnpj:<14} | {pagina}")

# Estatísticas
print("\nTotal de Páginas:", len(doc))
print("Total de Informações Extraídas:", len(dados_extraidos))
