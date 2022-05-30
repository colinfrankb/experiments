import psycopg2
import sshtunnel

server = sshtunnel.open_tunnel(
    ("ci3.sweepsouth.io" , 22),
    ssh_username="colinbob",
    ssh_pkey="/Users/colinbob/.ssh/id_ed25519",
    remote_bind_address=("connect-qa-master-do-user-4001697-0.db.ondigitalocean.com", 25060),
    local_bind_address=('0.0.0.0', 5432)
)

server.start()
print(server.local_bind_port)
print("tunnel opened. input any value to close")

# value = "open"
# while value == "open":
#     value = input()

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

server.stop()
