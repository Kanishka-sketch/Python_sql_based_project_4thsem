# Project Notes — Smart Interview Preparation Tracker

These notes summarize the design and architecture decisions made during development, intended as a quick reference for explaining the project in viva.

## 1. Problem Statement

Students preparing for placements track their progress across DSA practice, SQL practice, company research, and mock interviews — usually scattered across notebooks, spreadsheets, and multiple websites. There is no single place to see overall progress. This project centralizes all of this into one local desktop application with built-in analytics.

## 2. Architecture

```
Tkinter GUI (main.py)
       |
       v
Python modules (dsa.py, sql_tracker.py, company.py,
                mock_interview.py, user.py, analytics.py, charts.py)
       |
       v
PyODBC (db_connection.py)
       |
       v
SQL Server (InterviewTracker database, localhost\SQLEXPRESS)
```

This is a **layered architecture**:

- **Presentation layer (GUI)** — Tkinter, handles user input and displays data
- **Logic layer (Python modules)** — each module exposes functions (add/view/update/delete) for one entity
- **Data access layer** — `db_connection.py` centralizes the database connection so it isn't repeated in every module
- **Database layer** — SQL Server stores all persistent data

Each module follows the same pattern: open connection → execute query → process results → close connection. This consistency was deliberate — once one module (`dsa.py`) was written and tested, the rest (`sql_tracker.py`, `company.py`, `mock_interview.py`) followed the same template, just with different tables/columns.

## 3. Database Design

### Entity Relationship

```
Users (1) ----< (many) DSA_Problems
Users (1) ----< (many) SQL_Practice
Users (1) ----< (many) Companies
Users (1) ----< (many) Mock_Interviews
```

Each child table has a `user_id` foreign key referencing `Users.user_id`. This enforces **referential integrity** — a DSA problem, SQL topic, etc. cannot exist without belonging to a valid user.

### Why IDENTITY columns?

All primary keys use `INT IDENTITY(1,1)` — SQL Server auto-generates unique, incrementing IDs. Once an ID is used (even if the row is later deleted), it is never reused. This guarantees uniqueness across the table's lifetime, which matters if other tables ever reference that ID. Gaps in ID sequences after deletions are normal and expected in any real database design.

### Why parameterized queries (`?` placeholders)?

Every INSERT/UPDATE/DELETE/SELECT with user-supplied values uses `?` placeholders with PyODBC, rather than building SQL strings with string formatting. This prevents **SQL injection** — a security vulnerability where malicious input could alter the intended SQL command. PyODBC safely substitutes the values.

## 4. Single-User Design

The application is designed for a single user (the person running it on their own laptop) — there is no login screen. `USER_ID = 1` is hardcoded and used across all queries. This is a deliberate scope decision: the `Users` table and foreign key relationships still demonstrate proper relational design and could support multiple users in the future, but a login system was out of scope given the project timeline. Multi-user support is listed as a future enhancement.

## 5. GUI Design Decisions

- **`ttk` widgets** (not plain `tk`) were used throughout for a more modern look, with a custom dark theme applied via `ttk.Style`.
- **`ttk.Notebook`** provides a tabbed interface — one tab per module (DSA, SQL Practice, Company Prep, Mock Interviews, Analytics & Charts) — so the single window stays organized.
- **`ttk.Treeview`** displays tabular data (problems, topics, companies, interviews) in a spreadsheet-like view, refreshed after every add/update/delete so the UI always reflects the current database state.
- **`tkcalendar.DateEntry`** is used for date fields, giving a calendar picker while still producing a plain `YYYY-MM-DD` string that SQL Server accepts.
- **Input validation** (e.g., mock interview score must be an integer between 0–100) prevents invalid data from reaching the database.
- **`messagebox`** dialogs (info/warning/confirmation) give the user feedback for actions like successful adds, missing fields, and delete confirmations.

## 6. Analytics & Visualization

`analytics.py` contains aggregate queries (COUNT, AVG, GROUP BY) that summarize a user's progress:

- Total DSA problems solved
- Difficulty-wise distribution (Easy/Medium/Hard counts)
- Topic-wise problem counts
- Number of completed SQL topics
- Average mock interview score

`charts.py` uses these aggregates to generate Matplotlib visualizations:

- **Pie chart** — DSA problems by difficulty
- **Bar chart** — topic-wise problem counts

These are displayed via buttons on the Analytics & Charts tab and open in separate Matplotlib windows.

## 7. Development Approach

The project was built bottom-up, in this order:

1. Database schema and sample data
2. Database connection layer (`db_connection.py`)
3. CRUD modules for each entity (User, DSA, SQL, Company, Mock Interview)
4. Analytics module (aggregate queries)
5. Charts module (Matplotlib visualizations)
6. GUI (Tkinter), built tab-by-tab, reusing the same form + table + refresh pattern for each module

Building and testing the backend logic first (via simple `print()`-based test blocks) before building the GUI made debugging much easier — any error in the GUI could be isolated to GUI code, since the underlying database logic was already verified independently.

## 8. Future Enhancements

- **Daily streak tracking** — track consecutive days of practice
- **Goal tracking** — e.g., target of 300 problems, track progress toward it
- **Placement readiness score** — a composite score combining DSA, SQL, company prep, and mock interview progress
- **Report export** — generate PDF/text summaries of progress
- **Multi-user login** — allow multiple users to maintain separate progress records