import sqlite3, uuid, random
from faker import Faker
import pandas as pd

fake = Faker()

roles = pd.read_csv("/home/mtech/rishav/Asana_DataBuilder/data/fined_list_data/role.csv").iloc[:, 0].tolist()

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

teams = cur.execute("SELECT team_id, team_name FROM teams").fetchall()

for _ in range(5000):
    team_id, team_name = random.choice(teams)
    name = fake.name()
    email = name.lower().replace(" ", ".") + "@acme.com"

    cur.execute("""
        INSERT INTO users VALUES (?, ?, ?, ?, ?)
    """, (
        str(uuid.uuid4()),
        name,
        email,
        random.choice(roles),
        team_id
    ))

conn.commit()
conn.close()

print("5000  users inserted")