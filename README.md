# Asana Simulation Data Builder

## Overview

The **Asana Simulation Data Builder** is a Python-based project that generates a large-scale, realistic, Asana-like project management database using **SQLite**. It is designed for experimentation, analytics, SQL practice, backend testing, data science workflows, and research use cases where real Asana data is unavailable.

The project programmatically creates organizations, teams, users, projects, sections, tasks, and comments with realistic relationships and timestamps.

---

## Features

- Relational SQLite database simulating an Asana-like structure
- Large-scale synthetic data generation (thousands of users and tasks)
- Realistic timestamps, task status flows, and comments
- CSV-driven role, project, and task name generation
- Fully reproducible and extensible

---

## Database Schema

The generated database contains the following tables:

- `organizations`
- `teams`
- `users`
- `projects`
- `sections`
- `tasks`
- `comments`

Each table is linked using logical foreign-key-style relationships to closely resemble a real project management system.

---

## Tech Stack

- Python 3.9+
- SQLite
- Pandas
- NumPy
- Faker

---

##

---

## Setup Instructions

1. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the scripts sequentially to generate the database

```
python ./src/generators/creation.py
python ./src/generators/organizations.py
python ./src/generators/teams.py
python ./src/generators/users.py
python ./src/generators/projects.py
python ./src/generators/sections.py
python ./src/generators/tasks.py
python ./src/generators/comments.py
```

The SQLite database will be generated in the `output/` directory.

---

## Use Cases

- SQL query practice and interviews
- Data analytics and dashboarding
- Backend system prototyping
- Synthetic data generation for research
- Teaching relational databases

---

## Author

**Rishav Kumar**

---

## License

This project is intended for educational and research purposes.

