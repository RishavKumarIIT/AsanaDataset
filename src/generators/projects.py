import sqlite3, uuid, random
import pandas as pd
pnames = pd.read_csv("/home/mtech/rishav/Asana_DataBuilder/data/fined_list_data/project_name.csv").iloc[:, 0].tolist()
ptypes = pd.read_csv("/home/mtech/rishav/Asana_DataBuilder/data/fined_list_data/projectCategory_name.csv").iloc[:, 0].tolist()

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

teams = cur.execute("SELECT team_id, team_name FROM teams").fetchall()

for team_id, team_name in teams:


    for pname in pnames:
        cur.execute("""
            INSERT INTO projects VALUES (?, ?, ?, ?)
        """, (str(uuid.uuid4()), pname, random.choice(ptypes), team_id))

conn.commit()
conn.close()

print(" Projects inserted")