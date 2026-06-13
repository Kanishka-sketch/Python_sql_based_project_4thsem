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
        "FROM Mock_Interviews WHERE user_id = ? ORDER BY mock_id",
        (user_id,)
    )
    rows = cursor.fetchall()

    print("\n--- Mock Interviews ---")
    for row in rows:
        print(f"ID: {row.mock_id} | {row.mock_date} | Score: {row.score} | {row.feedback}")
    print("------------------------\n")

    cursor.close()
    conn.close()

def delete_mock_interview(mock_id):
    """Deletes a mock interview record by its ID."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("DELETE FROM Mock_Interviews WHERE mock_id = ?", (mock_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No mock interview found with ID {mock_id}.")
    else:
        print(f"Mock interview ID {mock_id} deleted successfully.")

    cursor.close()
    conn.close()

# Quick test
if __name__ == "__main__":
    view_mock_interviews(1)