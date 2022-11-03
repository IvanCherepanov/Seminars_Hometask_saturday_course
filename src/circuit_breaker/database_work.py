import psycopg2

con = psycopg2.connect(
    database="cism",
    user="user",
    password="password",
    host="127.0.0.1",
    port="5439"
)

print("Database opened successfully", "\n")
cur = con.cursor()
#cur.execute("SELECT id, pet_type_name from pet_type")
cur.execute("SELECT id, pet_type_name from pet_type where id=3")

rows = cur.fetchall()
for row in rows:
    print("id =", row[0])
    print("pet_type_name =", row[1], "\n")

print("Operation done successfully")

con.close()
