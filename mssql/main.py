# pip install pyodbc
# pip install python-dotenv

import os
import pyodbc
import csv
from dotenv import load_dotenv

load_dotenv()

# Variables
SERVER = os.getenv('SERVER')
DATABASE = os.getenv('DATABASE')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

# Connect
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={
    DATABASE};UID={USERNAME};PWD={PASSWORD};Encrypt=no;TrustServerCertificate=yes'
conn = pyodbc.connect(connectionString)

# First Query
SQL_QUERY_COUNT = """
SELECT COUNT(codigo) FROM cndcondo
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY_COUNT)
result = cursor.fetchone()[0]
print(f'Total de Condomínios: {result}')

# Second Query
SQL_QUERY = """
SELECT TOP 3 codigo, nome, nome_reduzido FROM cndcondo
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
row = cursor.fetchone()

with open('mssql.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ['Codigo', 'Nome', 'Nome Reduzido']
    writer.writerow(field)

    while row:
        print(row)
        writer.writerow(row)
        row = cursor.fetchone()
