import pyodbc

# Configurações de conexão
server = '192.168.0.8'  # Ex: 'localhost\\SQLEXPRESS'
database = 'banco'
username = 'usuario'
password = 'senha'

# Conexão com o SQL Server
try:
    conexao = pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    print("✅ Conexão bem-sucedida com o banco de dados!")

    cursor = conexao.cursor()
    cursor.execute(
        "SELECT usuario, nome, email, departamento, cargo FROM goUsuarios")

    linhas = cursor.fetchall()
    print(f"🔍 {len(linhas)} registros encontrados:\n")

    for linha in linhas:
        print(linha)

    cursor.close()
    conexao.close()

except Exception as e:
    print("❌ Erro ao conectar ou consultar:", e)
