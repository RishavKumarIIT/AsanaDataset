import sqlite3, uuid

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

projects = cur.execute("SELECT project_id FROM projects").fetchall()

for (pid,) in projects:
    for section in ["Backlog", "To Do", "In Progress", "In Review", "Done"]:
        cur.execute(
            "INSERT INTO sections VALUES (?, ?, ?)",
            (str(uuid.uuid4()), section, pid)
        )

conn.commit()
conn.close()

print(" Sections inserted")