import sqlite3

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS organizations;
DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS comments;

CREATE TABLE organizations (
    org_id TEXT PRIMARY KEY,
    org_name TEXT
);

CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    team_name TEXT,
    org_id TEXT
);

CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    name TEXT,
    email TEXT,
    role TEXT,
    team_id TEXT
);

CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    project_name TEXT,
    project_type TEXT,
    team_id TEXT
);

CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    section_name TEXT,
    project_id TEXT
);

CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    task_name TEXT,
    description TEXT,
    assignee_id TEXT,
    project_id TEXT,
    section_id TEXT,
    created_at TIMESTAMP,
    due_date DATE,
    completed_at TIMESTAMP,
    status TEXT
);

CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT,
    user_id TEXT,
    comment_text TEXT,
    created_at TIMESTAMP
);
""")

conn.commit()
conn.close()

print(" Schema created")



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




import sqlite3, uuid
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



import sqlite3, uuid, random
from faker import Faker
from datetime import timedelta

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



import sqlite3, uuid, random
from faker import Faker
from datetime import datetime # Import datetime

fake = Faker()

comment_templates = [
    "Please prioritize this.",
    "Blocked due to dependency.",
    "Looks good to me",
    "Waiting for QA validation.",
    "Customer reported this issue.",
    "Will be handled in next sprint.",
    "Needs product confirmation."
]

conn = sqlite3.connect("asana_simulation.sqlite")
cur = conn.cursor()

tasks = cur.execute("SELECT task_id, created_at FROM tasks").fetchall()
users = cur.execute("SELECT user_id FROM users").fetchall()

for task_id, created_at_str in tasks: # Renamed variable to avoid conflict
    if random.random() < 0.6:
        for _ in range(random.randint(1, 4)):
            # Convert created_at_str to a datetime object
            created_at_dt = datetime.fromisoformat(created_at_str)
            cur.execute("""
                INSERT INTO comments VALUES (?, ?, ?, ?, ?)
            """, (
                str(uuid.uuid4()),
                task_id,
                random.choice(users)[0],
                random.choice(comment_templates),
                fake.date_time_between(start_date=created_at_dt, end_date="now")
            ))

conn.commit()
conn.close()

print(" Comments inserted")





import pandas as pd
import sqlite3

# Update path to match your project structure
db_path = "/home/mtech/rishav/Asana_DataBuilder/output/asana_simulation.sqlite"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 1. Get a list of all table names in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print(f"\n{'='*60}")
print(f"--- Found {len(tables)} tables in the Asana Simulation Database ---")
print(f"{'='*60}\n")

# 2. Loop through and print each table individually
for table_name in tables:
    name = table_name[0]
    
    # Skip internal sqlite metadata tables
    if name == 'sqlite_sequence':
        continue
        
    print(f"--- TABLE: {name.upper()} ---")
    
    # Read the table into a DataFrame
    df = pd.read_sql(f"SELECT * FROM {name}", conn)
    
    # Check if table is empty
    if df.empty:
        print("[Empty Table]")
    else:
        # head(20) like a Result Grid
        # to_string() ensures the table doesn't get truncated in the terminal
        print(df.head(20).to_string(index=False))
        print(f"\nTotal Cells (Size): {df.size}")
        print(f"Total Rows: {len(df)}")
    
    print("-" * 60)

conn.close()
