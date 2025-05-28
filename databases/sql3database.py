import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = "db.sqlite3"
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "customers"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight)'
    'VALUES (?, ?)'
)

# sql = (
#     f'INSERT INTO {TABLE_NAME} (name, weight)'
#     'VALUES (:nome, :peso)'
# )

cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)

# cursor.execute(sql, {nome: 'Fulano', 'peso': 10})
# cursor.executemany(sql, (
#     {'nome': 'Nome 1', 'peso': 1},
#     {'nome': 'Nome 2', 'peso': 2},
# ))
# cursor.execute(sql, ['Fulano', 5])
# cursor.executemany(sql, [['Ciclano', 3], ['Beltrano', 8]])
cursor.execute(
    f'INSERT INTO {TABLE_NAME} (id, name, weight)'
    'VALUES (NULL, "Alan Silva", 9.5), (NULL, "Rafael Garcia", 1.2)'
)

cursor.execute(
    f'UPDATE {TABLE_NAME} SET name = "Alan Silva Update" WHERE id = 1'
)

cursor.execute(f'SELECT * FROM {TABLE_NAME}')

rows = cursor.fetchall()

connection.commit()
cursor.close()
connection.close()

# for row in rows:
#     print(row)

if __name__ == '__main__':
    print(sql)
    for row in rows:
        print(row)
