from db_connection import get_connection

def add_topic(user_id, topic, difficulty, practice_date, status):
    """Inserts a new SQL practice topic."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO SQL_Practice (user_id, topic, difficulty, practice_date, status) "
        "VALUES (?, ?, ?, ?, ?)",
        (user_id, topic, difficulty, practice_date, status)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"SQL topic '{topic}' added successfully.")


def update_status(sql_id, new_status):
    """Updates the status of a SQL practice topic."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE SQL_Practice SET status = ? WHERE sql_id = ?",
        (new_status, sql_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No SQL topic found with ID {sql_id}.")
    else:
        print(f"SQL topic ID {sql_id} status updated to '{new_status}'.")

    cursor.close()
    conn.close()


def view_topics(user_id):
    """Fetches and prints all SQL practice topics for a given user."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "SELECT sql_id, topic, difficulty, practice_date, status "
        "FROM SQL_Practice WHERE user_id = ? ORDER BY sql_id",
        (user_id,)
    )
    rows = cursor.fetchall()

    print("\n--- SQL Practice Topics ---")
    for row in rows:
        print(f"ID: {row.sql_id} | {row.topic} | {row.difficulty} | "
              f"{row.practice_date} | {row.status}")
    print("---------------------------\n")

    cursor.close()
    conn.close()

def delete_topic(sql_id):
    """Deletes a SQL practice topic by its ID."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("DELETE FROM SQL_Practice WHERE sql_id = ?", (sql_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No topic found with ID {sql_id}.")
    else:
        print(f"Topic ID {sql_id} deleted successfully.")

    cursor.close()
    conn.close()
    
# Quick test
if __name__ == "__main__":
    view_topics(1)