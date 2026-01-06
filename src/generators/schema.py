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