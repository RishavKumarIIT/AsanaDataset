import sqlite3, uuid

teams = [
    "Backend Platform",
    "Mobile Apps",
    "Web Frontend",
    "QA & Automation",
    "DevOps",
    "Product Management",
    "Design",
    "Marketing",
    "Growth",
    "Customer Support",
    "Operations"
]

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

org_id = cur.execute("SELECT org_id FROM organizations").fetchone()[0]

for team in teams:
    cur.execute(
        "INSERT INTO teams VALUES (?, ?, ?)",
        (str(uuid.uuid4()), team, org_id)
    )

conn.commit()
conn.close()

print(" Teams inserted")