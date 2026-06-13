from db_connection import get_connection

def add_mock_interview(user_id, mock_date, score, feedback):
    """Inserts a new mock interview record."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Mock_Interviews (user_id, mock_date, score, feedback) "
        "VALUES (?, ?, ?, ?)",
        (user_id, mock_date, score, feedback)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print("Mock interview record added successfully.")


def view_mock_interviews(user_id):
    """Fetches and prints all mock interview records for a given user."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "SELECT mock_id, mock_date, score, feedback "
        "FROM Mock_Interviews WHERE user_id = ?",
        (user_id,)
    )
    rows = cursor.fetchall()

    print("\n--- Mock Interviews ---")
    for row in rows:
        print(f"ID: {row.mock_id} | {row.mock_date} | Score: {row.score} | {row.feedback}")
    print("------------------------\n")

    cursor.close()
    conn.close()


# Quick test
if __name__ == "__main__":
    view_mock_interviews(1)