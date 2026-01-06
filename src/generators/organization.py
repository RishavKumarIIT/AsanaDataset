import sqlite3, uuid

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

cur.execute(
    "INSERT INTO organizations VALUES (?, ?)",
    (str(uuid.uuid4()), "Acme SaaS Corporation")
)

conn.commit()
conn.close()

print(" Organization inserted")