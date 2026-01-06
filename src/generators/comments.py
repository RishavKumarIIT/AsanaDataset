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