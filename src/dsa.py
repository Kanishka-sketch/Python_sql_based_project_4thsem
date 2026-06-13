from db_connection import get_connection

def add_problem(user_id, problem_name, difficulty, topic, platform, date_solved):
    """Inserts a new DSA problem record."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO DSA_Problems (user_id, problem_name, difficulty, topic, platform, date_solved) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, problem_name, difficulty, topic, platform, date_solved)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Problem '{problem_name}' added successfully.")


def view_problems(user_id):
    """Fetches and prints all DSA problems for a given user."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "SELECT problem_id, problem_name, difficulty, topic, platform, date_solved "
        "FROM DSA_Problems WHERE user_id = ? ORDER BY problem_id",
        (user_id,)
    )
    rows = cursor.fetchall()

    print("\n--- DSA Problems ---")
    for row in rows:
        print(f"ID: {row.problem_id} | {row.problem_name} | {row.difficulty} | "
              f"{row.topic} | {row.platform} | {row.date_solved}")
    print("--------------------\n")

    cursor.close()
    conn.close()


def delete_problem(problem_id):
    """Deletes a DSA problem by its ID."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("DELETE FROM DSA_Problems WHERE problem_id = ?", (problem_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No problem found with ID {problem_id}.")
    else:
        print(f"Problem ID {problem_id} deleted successfully.")

    cursor.close()
    conn.close()


# # Quick test
# if __name__ == "__main__":
#     view_problems(1)

# # Quick test
# if __name__ == "__main__":
#     add_problem(1, "Test Problem", "Easy", "Array", "LeetCode", "2026-06-13")
#     view_problems(1)
#     delete_problem(5)  # deletes the test problem we just added (should be ID 5)
#     view_problems(1)