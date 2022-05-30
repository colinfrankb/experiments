import psycopg2

conn = psycopg2.connect(
    database="sweepsouth_connect",
    user="prathiksha",
    host='localhost',
    port=5432,
    password="fkxpWPl5OBEL")

cur = conn.cursor()

cur.execute("select * from service_provider limit 1;")
data = cur.fetchall()
print(data)