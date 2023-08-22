# NÃO DEU CERTO AINDA, MAS ESTOU NO CAMINHO.

import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "Aula-1/aplicacao-whatsapp-fase-1.sql"
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor()

with open("aplicacao-whatsapp-fase-1.sql") as sql_file:
    queries = sql_file.read()

query_list = queries.split(';')

for query in query_list:
    if query.strip():
        cursor.execute(query)
        conn.commit()

cursor.close()

conn.close()
