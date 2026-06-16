import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Smart Interview Preparation Tracker")
root.geometry("900x650")

# --- Color palette (Dark Navy theme) ---
BG_COLOR = "#1B2430"        # main background
SURFACE_COLOR = "#222B38"   # tab content background
CARD_COLOR = "#262F3D"      # form/labelframe background
HEADER_COLOR = "#11161F"    # top header bar
ACCENT_COLOR = "#2D6CDF"    # blue accent (selected tab, buttons)
BORDER_COLOR = "#3A4556"
TEXT_LIGHT = "#E8EAED"
TEXT_MUTED = "#9AA4B2"
DANGER_COLOR = "#E24B4A"

root.configure(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")

# General widget styles
style.configure("TFrame", background=SURFACE_COLOR)
style.configure("TLabel", background=SURFACE_COLOR, foreground=TEXT_LIGHT, font=("Segoe UI", 10))
style.configure("TLabelframe", background=SURFACE_COLOR, foreground=TEXT_LIGHT, bordercolor=BORDER_COLOR)
style.configure("TLabelframe.Label", background=SURFACE_COLOR, foreground=TEXT_MUTED, font=("Segoe UI", 10))

style.configure("TEntry", fieldbackground=CARD_COLOR, foreground=TEXT_LIGHT,
                bordercolor=BORDER_COLOR, insertcolor=TEXT_LIGHT)
style.configure("TCombobox", fieldbackground=CARD_COLOR, background=CARD_COLOR,
                foreground=TEXT_LIGHT, bordercolor=BORDER_COLOR)

# Heading style (section titles)
style.configure("Heading.TLabel", background=SURFACE_COLOR, foreground=ACCENT_COLOR,
                font=("Segoe UI", 12, "bold"))

# Buttons
style.configure("TButton", font=("Segoe UI", 10), padding=6,
                background=CARD_COLOR, foreground=TEXT_LIGHT, bordercolor=BORDER_COLOR)
style.map("TButton", background=[("active", ACCENT_COLOR)])

# Danger (delete) button
style.configure("Danger.TButton", font=("Segoe UI", 10), padding=6,
                background=DANGER_COLOR, foreground="white", bordercolor=DANGER_COLOR)
style.map("Danger.TButton", background=[("active", "#C13B3A")])

# Notebook (tabs)
style.configure("TNotebook", background=BG_COLOR, bordercolor=BORDER_COLOR)
style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[14, 8],
                background=CARD_COLOR, foreground=TEXT_MUTED)
style.map("TNotebook.Tab",
          background=[("selected", ACCENT_COLOR)],
          foreground=[("selected", "white")])

# Treeview (tables)
style.configure("Treeview",
                background=CARD_COLOR, foreground=TEXT_LIGHT,
                fieldbackground=CARD_COLOR, bordercolor=BORDER_COLOR,
                rowheight=26, font=("Segoe UI", 10))
style.configure("Treeview.Heading",
                background=HEADER_COLOR, foreground=TEXT_MUTED,
                font=("Segoe UI", 10, "bold"))
style.map("Treeview", background=[("selected", ACCENT_COLOR)],
          foreground=[("selected", "white")])

# --- Header bar ---
header = tk.Frame(root, bg=HEADER_COLOR, height=60)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="Smart Interview Preparation Tracker",
    bg=HEADER_COLOR,
    fg=TEXT_LIGHT,
    font=("Segoe UI", 16, "bold"),
    pady=15
)
title_label.pack()

# Current user (Option A - hardcoded single user)
USER_ID = 1

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=10, pady=10)

dsa_tab = ttk.Frame(notebook, padding=15)
sql_tab = ttk.Frame(notebook, padding=15)
company_tab = ttk.Frame(notebook, padding=15)
mock_tab = ttk.Frame(notebook, padding=15)
analytics_tab = ttk.Frame(notebook, padding=15)

notebook.add(dsa_tab, text="DSA Tracker")
notebook.add(sql_tab, text="SQL Practice")
notebook.add(company_tab, text="Company Prep")
notebook.add(mock_tab, text="Mock Interviews")
notebook.add(analytics_tab, text="Analytics & Charts")


#==========DSA TRACKER TAB ==============
from dsa import add_problem, view_problems, delete_problem
from db_connection import get_connection
from tkinter import messagebox

# ============ DSA TAB ============

# --- Form section ---
dsa_form = ttk.LabelFrame(dsa_tab, text="Add New DSA Problem", padding=15)
dsa_form.pack(fill="x", pady=(0, 15))

ttk.Label(dsa_form, text="Problem Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
dsa_name_entry = ttk.Entry(dsa_form, width=30)
dsa_name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(dsa_form, text="Difficulty:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
dsa_difficulty_combo = ttk.Combobox(dsa_form, values=["Easy", "Medium", "Hard"], width=15, state="readonly")
dsa_difficulty_combo.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(dsa_form, text="Topic:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
dsa_topic_entry = ttk.Entry(dsa_form, width=30)
dsa_topic_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(dsa_form, text="Platform:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
dsa_platform_entry = ttk.Entry(dsa_form, width=15)
dsa_platform_entry.grid(row=1, column=3, padx=5, pady=5)

from tkcalendar import DateEntry

ttk.Label(dsa_form, text="Date Solved:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
dsa_date_entry = DateEntry(dsa_form, width=27, date_pattern="yyyy-mm-dd", background='darkblue', foreground='white',borderwidth=2)
dsa_date_entry.grid(row=2, column=1, padx=5, pady=5)


def handle_add_problem():
    name = dsa_name_entry.get().strip()
    difficulty = dsa_difficulty_combo.get().strip()
    topic = dsa_topic_entry.get().strip()
    platform = dsa_platform_entry.get().strip()
    date = dsa_date_entry.get().strip()

    if not all([name, difficulty, topic, platform, date]):
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return

    add_problem(USER_ID, name, difficulty, topic, platform, date)
    messagebox.showinfo("Success", f"Problem '{name}' added successfully!")

    # Clear fields
    dsa_name_entry.delete(0, tk.END)
    dsa_difficulty_combo.set("")
    dsa_topic_entry.delete(0, tk.END)
    dsa_platform_entry.delete(0, tk.END)
    dsa_date_entry.delete(0, tk.END)

    refresh_dsa_table()


ttk.Button(dsa_form, text="Add Problem", command=handle_add_problem).grid(row=2, column=3, padx=5, pady=10)

# --- Table section ---
ttk.Label(dsa_tab, text="Your DSA Problems", style="Heading.TLabel").pack(anchor="w", pady=(0, 5))

dsa_columns = ("ID", "Problem Name", "Difficulty", "Topic", "Platform", "Date Solved")
dsa_tree = ttk.Treeview(dsa_tab, columns=dsa_columns, show="headings", height=10)

for col in dsa_columns:
    dsa_tree.heading(col, text=col)
    dsa_tree.column(col, width=120, anchor="center")

dsa_tree.pack(fill="both", expand=True, pady=(0, 10))


def refresh_dsa_table():
    # Clear existing rows
    for row in dsa_tree.get_children():
        dsa_tree.delete(row)

    # Fetch fresh data directly (reusing logic similar to view_problems)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT problem_id, problem_name, difficulty, topic, platform, date_solved "
        "FROM DSA_Problems WHERE user_id = ? ORDER BY problem_id",
        (USER_ID,)
    )
    for row in cursor.fetchall():
        dsa_tree.insert("", tk.END, values=(row.problem_id, row.problem_name, row.difficulty, row.topic, row.platform, row.date_solved))
    cursor.close()
    conn.close()


def handle_delete_problem():
    selected = dsa_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a problem to delete.")
        return

    item = dsa_tree.item(selected[0])
    problem_id = item["values"][0]

    confirm = messagebox.askyesno("Confirm Delete", f"Delete problem ID {problem_id}?")
    if confirm:
        delete_problem(problem_id)
        refresh_dsa_table()


# --- Buttons below table ---
dsa_button_frame = ttk.Frame(dsa_tab)
dsa_button_frame.pack(fill="x")

ttk.Button(dsa_button_frame, text="Refresh", command=refresh_dsa_table).pack(side="left", padx=5)
ttk.Button(dsa_button_frame, text="Delete Selected", command=handle_delete_problem).pack(side="left", padx=5)

# Load data on startup
refresh_dsa_table()


# ============ SQL PRACTICE TAB ============

from sql_tracker import add_topic, update_status , delete_topic

# --- Form section ---
sql_form = ttk.LabelFrame(sql_tab, text="Add New SQL Practice Topic", padding=15)
sql_form.pack(fill="x", pady=(0, 15))

ttk.Label(sql_form, text="Topic:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
sql_topic_entry = ttk.Entry(sql_form, width=30)
sql_topic_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(sql_form, text="Difficulty:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
sql_difficulty_combo = ttk.Combobox(sql_form, values=["Easy", "Medium", "Hard"], width=15, state="readonly")
sql_difficulty_combo.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(sql_form, text="Practice Date:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
sql_date_entry = DateEntry(sql_form, width=27, date_pattern="yyyy-mm-dd")
sql_date_entry.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(sql_form, text="Status:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
sql_status_combo = ttk.Combobox(sql_form, values=["Not Started", "In Progress", "Completed"], width=15, state="readonly")
sql_status_combo.grid(row=1, column=3, padx=5, pady=5)


def handle_add_topic():
    topic = sql_topic_entry.get().strip()
    difficulty = sql_difficulty_combo.get().strip()
    date = sql_date_entry.get().strip()
    status = sql_status_combo.get().strip()

    if not all([topic, difficulty, date, status]):
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return

    add_topic(USER_ID, topic, difficulty, date, status)
    messagebox.showinfo("Success", f"Topic '{topic}' added successfully!")

    sql_topic_entry.delete(0, tk.END)
    sql_difficulty_combo.set("")
    sql_status_combo.set("")

    refresh_sql_table()


ttk.Button(sql_form, text="Add Topic", command=handle_add_topic).grid(row=2, column=3, padx=5, pady=10)

# --- Table section ---
ttk.Label(sql_tab, text="Your SQL Practice Topics", style="Heading.TLabel").pack(anchor="w", pady=(0, 5))

sql_columns = ("ID", "Topic", "Difficulty", "Practice Date", "Status")
sql_tree = ttk.Treeview(sql_tab, columns=sql_columns, show="headings", height=10)

for col in sql_columns:
    sql_tree.heading(col, text=col)
    sql_tree.column(col, width=130, anchor="center")

sql_tree.pack(fill="both", expand=True, pady=(0, 10))


def refresh_sql_table():
    for row in sql_tree.get_children():
        sql_tree.delete(row)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT sql_id, topic, difficulty, practice_date, status "
        "FROM SQL_Practice WHERE user_id = ? ORDER BY sql_id",
        (USER_ID,)
    )
    for row in cursor.fetchall():
        sql_tree.insert("", tk.END, values=(row.sql_id, row.topic, row.difficulty,
                                              row.practice_date, row.status))
    cursor.close()
    conn.close()


def handle_update_status():
    selected = sql_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a topic to update.")
        return

    item = sql_tree.item(selected[0])
    sql_id = item["values"][0]
    new_status = sql_status_combo.get().strip()

    if not new_status:
        messagebox.showwarning("No Status", "Please select a status from the dropdown above first.")
        return

    update_status(sql_id, new_status)
    refresh_sql_table()

def handle_delete_topic():
    selected = sql_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a topic to delete.")
        return

    item = sql_tree.item(selected[0])
    sql_id = item["values"][0]

    confirm = messagebox.askyesno("Confirm Delete", f"Delete topic ID {sql_id}?")
    if confirm:
        delete_topic(sql_id)
        refresh_sql_table()

# --- Buttons below table ---
sql_button_frame = ttk.Frame(sql_tab)
sql_button_frame.pack(fill="x")

ttk.Button(sql_button_frame, text="Refresh", command=refresh_sql_table).pack(side="left", padx=5)
ttk.Button(sql_button_frame, text="Update Status of Selected", command=handle_update_status).pack(side="left", padx=5)
ttk.Button(sql_button_frame, text="Delete Selected", command=handle_delete_topic).pack(side="left", padx=5)

# Load data on startup
refresh_sql_table()

#=============================================
from company import add_company, update_company_status, delete_company

# ============ COMPANY PREP TAB ============

# --- Form section ---
company_form = ttk.LabelFrame(company_tab, text="Add New Company", padding=15)
company_form.pack(fill="x", pady=(0, 15))

ttk.Label(company_form, text="Company Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
company_name_entry = ttk.Entry(company_form, width=30)
company_name_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(company_form, text="Status:").grid(row=0, column=2, sticky="w", padx=5, pady=5)
company_status_combo = ttk.Combobox(company_form, values=["Not Started", "In Progress", "Completed"], width=15, state="readonly")
company_status_combo.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(company_form, text="Notes:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
company_notes_entry = ttk.Entry(company_form, width=50)
company_notes_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")


def handle_add_company():
    name = company_name_entry.get().strip()
    status = company_status_combo.get().strip()
    notes = company_notes_entry.get().strip()

    if not all([name, status]):
        messagebox.showwarning("Missing Data", "Please fill in Company Name and Status.")
        return

    add_company(USER_ID, name, status, notes)
    messagebox.showinfo("Success", f"Company '{name}' added successfully!")

    company_name_entry.delete(0, tk.END)
    company_status_combo.set("")
    company_notes_entry.delete(0, tk.END)

    refresh_company_table()


ttk.Button(company_form, text="Add Company", command=handle_add_company).grid(row=2, column=3, padx=5, pady=10)

# --- Table section ---
ttk.Label(company_tab, text="Your Company Preparation", style="Heading.TLabel").pack(anchor="w", pady=(0, 5))

company_columns = ("ID", "Company Name", "Status", "Notes")
company_tree = ttk.Treeview(company_tab, columns=company_columns, show="headings", height=10)

company_tree.column("ID", width=50, anchor="center")
company_tree.column("Company Name", width=150, anchor="center")
company_tree.column("Status", width=120, anchor="center")
company_tree.column("Notes", width=300, anchor="w")

for col in company_columns:
    company_tree.heading(col, text=col)

company_tree.pack(fill="both", expand=True, pady=(0, 10))


def refresh_company_table():
    for row in company_tree.get_children():
        company_tree.delete(row)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT company_id, company_name, status, notes "
        "FROM Companies WHERE user_id = ? ORDER BY company_id",
        (USER_ID,)
    )
    for row in cursor.fetchall():
        company_tree.insert("", tk.END, values=(row.company_id, row.company_name, row.status, row.notes))
    cursor.close()
    conn.close()


def handle_update_company_status():
    selected = company_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a company to update.")
        return

    item = company_tree.item(selected[0])
    company_id = item["values"][0]
    new_status = company_status_combo.get().strip()

    if not new_status:
        messagebox.showwarning("No Status", "Please select a status from the dropdown above first.")
        return

    update_company_status(company_id, new_status)
    refresh_company_table()


def handle_delete_company():
    selected = company_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a company to delete.")
        return

    item = company_tree.item(selected[0])
    company_id = item["values"][0]

    confirm = messagebox.askyesno("Confirm Delete", f"Delete company ID {company_id}?")
    if confirm:
        delete_company(company_id)
        refresh_company_table()


# --- Buttons below table ---
company_button_frame = ttk.Frame(company_tab)
company_button_frame.pack(fill="x")

ttk.Button(company_button_frame, text="Refresh", command=refresh_company_table).pack(side="left", padx=5)
ttk.Button(company_button_frame, text="Update Status of Selected", command=handle_update_company_status).pack(side="left", padx=5)
ttk.Button(company_button_frame, text="Delete Selected", command=handle_delete_company).pack(side="left", padx=5)

# Load data on startup
refresh_company_table()

#============================================
from mock_interview import add_mock_interview, delete_mock_interview

# ============ MOCK INTERVIEWS TAB ============

# --- Form section ---
mock_form = ttk.LabelFrame(mock_tab, text="Add New Mock Interview", padding=15)
mock_form.pack(fill="x", pady=(0, 15))

ttk.Label(mock_form, text="Mock Date:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
mock_date_entry = DateEntry(mock_form, width=27, date_pattern="yyyy-mm-dd")
mock_date_entry.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(mock_form, text="Score (0-100):").grid(row=0, column=2, sticky="w", padx=5, pady=5)
mock_score_entry = ttk.Entry(mock_form, width=15)
mock_score_entry.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(mock_form, text="Feedback:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
mock_feedback_entry = ttk.Entry(mock_form, width=50)
mock_feedback_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="w")


def handle_add_mock():
    date = mock_date_entry.get().strip()
    score = mock_score_entry.get().strip()
    feedback = mock_feedback_entry.get().strip()

    if not all([date, score, feedback]):
        messagebox.showwarning("Missing Data", "Please fill in all fields.")
        return

    try:
        score = int(score)
        if not (0 <= score <= 100):
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Score", "Score must be a whole number between 0 and 100.")
        return

    add_mock_interview(USER_ID, date, score, feedback)
    messagebox.showinfo("Success", "Mock interview record added successfully!")

    mock_score_entry.delete(0, tk.END)
    mock_feedback_entry.delete(0, tk.END)

    refresh_mock_table()


ttk.Button(mock_form, text="Add Record", command=handle_add_mock).grid(row=2, column=3, padx=5, pady=10)

# --- Table section ---
ttk.Label(mock_tab, text="Your Mock Interviews", style="Heading.TLabel").pack(anchor="w", pady=(0, 5))

mock_columns = ("ID", "Date", "Score", "Feedback")
mock_tree = ttk.Treeview(mock_tab, columns=mock_columns, show="headings", height=10)

mock_tree.column("ID", width=50, anchor="center")
mock_tree.column("Date", width=120, anchor="center")
mock_tree.column("Score", width=80, anchor="center")
mock_tree.column("Feedback", width=350, anchor="w")

for col in mock_columns:
    mock_tree.heading(col, text=col)

mock_tree.pack(fill="both", expand=True, pady=(0, 10))


def refresh_mock_table():
    for row in mock_tree.get_children():
        mock_tree.delete(row)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT mock_id, mock_date, score, feedback "
        "FROM Mock_Interviews WHERE user_id = ? ORDER BY mock_id",
        (USER_ID,)
    )
    for row in cursor.fetchall():
        mock_tree.insert("", tk.END, values=(row.mock_id, row.mock_date, row.score, row.feedback))
    cursor.close()
    conn.close()


def handle_delete_mock():
    selected = mock_tree.selection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a record to delete.")
        return

    item = mock_tree.item(selected[0])
    mock_id = item["values"][0]

    confirm = messagebox.askyesno("Confirm Delete", f"Delete mock interview ID {mock_id}?")
    if confirm:
        delete_mock_interview(mock_id)
        refresh_mock_table()


# --- Buttons below table ---
mock_button_frame = ttk.Frame(mock_tab)
mock_button_frame.pack(fill="x")

ttk.Button(mock_button_frame, text="Refresh", command=refresh_mock_table).pack(side="left", padx=5)
ttk.Button(mock_button_frame, text="Delete Selected", command=handle_delete_mock).pack(side="left", padx=5)

# Load data on startup
refresh_mock_table()

#===============================================
from analytics import (total_problems_solved, difficulty_distribution,
                        topic_wise_count, completed_sql_topics, average_mock_score)
from charts import show_difficulty_pie_chart, show_topic_bar_chart

# ============ ANALYTICS & CHARTS TAB ============

ttk.Label(analytics_tab, text="Your Progress Summary", style="Heading.TLabel").pack(anchor="w", pady=(0, 15))

# --- Stats display frame ---
stats_frame = ttk.LabelFrame(analytics_tab, text="Statistics", padding=20)
stats_frame.pack(fill="x", pady=(0, 20))

stat_total_problems = ttk.Label(stats_frame, text="Total Problems Solved: -", font=("Segoe UI", 11))
stat_total_problems.grid(row=0, column=0, sticky="w", padx=10, pady=8)

stat_sql_completed = ttk.Label(stats_frame, text="Completed SQL Topics: -", font=("Segoe UI", 11))
stat_sql_completed.grid(row=1, column=0, sticky="w", padx=10, pady=8)

stat_avg_score = ttk.Label(stats_frame, text="Average Mock Interview Score: -", font=("Segoe UI", 11))
stat_avg_score.grid(row=2, column=0, sticky="w", padx=10, pady=8)

stat_difficulty = ttk.Label(stats_frame, text="Difficulty Breakdown: -", font=("Segoe UI", 11))
stat_difficulty.grid(row=3, column=0, sticky="w", padx=10, pady=8)

stat_topic_wise = ttk.Label(stats_frame, text="Topic-wise Count: -", font=("Segoe UI", 11))
stat_topic_wise.grid(row=4, column=0, sticky="w", padx=10, pady=8)

def refresh_analytics():
    total = total_problems_solved(USER_ID)
    sql_completed = completed_sql_topics(USER_ID)
    avg_score = average_mock_score(USER_ID)
    diff_dist = difficulty_distribution(USER_ID)
    topic_dist = topic_wise_count(USER_ID)

    stat_total_problems.config(text=f"Total Problems Solved: {total}")
    stat_sql_completed.config(text=f"Completed SQL Topics: {sql_completed}")
    stat_avg_score.config(text=f"Average Mock Interview Score: {avg_score:.1f}")

    diff_text = ", ".join([f"{d}: {c}" for d, c in diff_dist]) if diff_dist else "No data yet"
    stat_difficulty.config(text=f"Difficulty Breakdown: {diff_text}")

    topic_text = ", ".join([f"{t}: {c}" for t, c in topic_dist]) if topic_dist else "No data yet"
    stat_topic_wise.config(text=f"Topic-wise Count: {topic_text}")


ttk.Button(stats_frame, text="Refresh Stats", command=refresh_analytics).grid(row=5, column=0, sticky="w", padx=10, pady=10)

# --- Charts frame ---
charts_frame = ttk.LabelFrame(analytics_tab, text="Visualizations", padding=20)
charts_frame.pack(fill="x")

ttk.Label(charts_frame, text="Click a button below to open a chart in a new window:",
          font=("Segoe UI", 10)).pack(anchor="w", pady=(0, 10))

chart_button_frame = ttk.Frame(charts_frame)
chart_button_frame.pack(anchor="w")

ttk.Button(chart_button_frame, text="Show Difficulty Pie Chart",
           command=lambda: show_difficulty_pie_chart(USER_ID)).pack(side="left", padx=5)

ttk.Button(chart_button_frame, text="Show Topic-wise Bar Chart",
           command=lambda: show_topic_bar_chart(USER_ID)).pack(side="left", padx=5)

# Load stats on startup
refresh_analytics()

root.mainloop()