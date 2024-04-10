import pyodbc

SERVER = '192.168.0.8'
DATABASE = 'sigadm'
USERNAME = 'apiuser'
PASSWORD = 'Kilo51000?'

connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD};Encrypt=no;TrustServerCertificate=yes'
conn = pyodbc.connect(connectionString) 

SQL_QUERY_COUNT = """
SELECT COUNT(codigo) FROM cndcondo
"""

cursor = conn.cursor()
cursor.execute(SQL_QUERY_COUNT)  
result = cursor.fetchone()[0]
print(f'Total de Condomínios: {result}')

SQL_QUERY = """
SELECT codigo, nome, nome_reduzido FROM cndcondo
"""

cursor = conn.cursor()	
cursor.execute(SQL_QUERY) 
row = cursor.fetchone() 
while row:
    print(row) 
    row = cursor.fetchone()