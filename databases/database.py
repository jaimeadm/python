import pymysql
import pymysql.cursors
import dotenv
import os

TABLE_NAME = 'customers'
CURRENT_CURSOR = pymysql.cursors.DictCursor

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4',
    cursorclass=CURRENT_CURSOR,
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS customers ('
            'id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL '
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
        connection.commit()

        # Começo a manipular dados a partir daqui

        with connection.cursor() as cursor:
            cursor.execute(  # type: ignore
                f'INSERT INTO {TABLE_NAME} '
                '(nome, idade) VALUES ("Luiz", 25) '
            )
            sql = (
                f'INSERT INTO {TABLE_NAME} '
                '(nome, idade) '
                'VALUES '
                '(%s, %s) '
            )
            data = ('João', 30)
            result = cursor.execute(sql, data)
            print(sql, data)
            result = cursor.execute(  # type: ignore
                f'INSERT INTO {TABLE_NAME} '
                '(nome, idade) VALUES ("Maria", 45) '
            )
            print(result)
        connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s)'
        )
        dado = {
            "nome": "Rose",
            "idade": 45,
        }
        result = cursor.execute(sql, dado)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s)'
        )
        valores = (
            ("Fulano", 34, ),
            ("Ciclano", 20, ),
            ("Beltrano", 53, ),
        )
        result = cursor.executemany(sql, valores)
        print(sql)
        print(valores)
        print(result)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'SELECT id, nome, idade FROM {TABLE_NAME} '
        )
        cursor.execute(sql)
        data10 = cursor.fetchall()

        for row in data10:
            print(row)

    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (1,))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row in cursor.fetchall():
            print(row)

    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome = %s, idade = %s '
            'WHERE id = %s'
        )
        cursor.execute(sql, ('Claudia', 15, 7))

        cursor.execute(
            f'SELECT id from {TABLE_NAME} ORDER BY id DESC LIMIT 1'
        )
        lastIdFromSelect = cursor.fetchone()

        resultFromSelect = cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        data6 = cursor.fetchall()

        for row in data6:
            print(row)

        print('resultFromSelect', resultFromSelect)
        print('len(data6)', len(data6))
        print('rowcount', cursor.rowcount)
        print('lastrowid', cursor.lastrowid)
        print('lastrowid na mão', lastIdFromSelect)

        cursor.scroll(0, 'absolute')
        print('rownumber', cursor.rownumber)

    connection.commit()
