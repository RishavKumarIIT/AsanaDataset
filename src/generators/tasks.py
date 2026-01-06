import sqlite3, uuid, random
from faker import Faker
from datetime import timedelta
import pandas as pd

fake = Faker()

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()
task_name = pd.read_csv("/home/mtech/rishav/Asana_DataBuilder/data/fined_list_data/task.csv").iloc[:, 0].tolist()
task_desc = pd.read_csv("/home/mtech/rishav/Asana_DataBuilder/data/fined_list_data/projectCategory_description.csv").iloc[:, 0].tolist()

users = cur.execute("SELECT user_id FROM users").fetchall()
projects = cur.execute("SELECT project_id FROM projects").fetchall()
sections = cur.execute("SELECT section_id, project_id FROM sections").fetchall()

task_patterns = [
    "Fix {component} bug",
    "Implement {feature}",
    "Improve {component} performance",
    "Investigate {issue}",
    "Refactor {component}",
]

components = ["login flow", "payment API", "search service", "UI rendering"]
features = ["OTP", "caching", "rate limiting"]
issues = ["timeout", "crash", "edge case"]

for name in task_name:
    project_id = random.choice(projects)[0]
    section_id = random.choice([s[0] for s in sections if s[1] == project_id])

    created = fake.date_time_between(start_date="-6M", end_date="now")
    completed = random.random() < 0.65

    cur.execute("""
        INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        str(uuid.uuid4()),
        name,
        random.choice(task_desc),
        None if random.random() < 0.15 else random.choice(users)[0],
        project_id,
        section_id,
        created,
        created + timedelta(days=random.randint(5, 40)),
        created + timedelta(days=random.randint(2, 25)) if completed else None,
        "Done" if completed else "In Progress"
    ))

conn.commit()
conn.close()

print(" Tasks inserted")