from db_connection import get_connection

def add_user(name, email, college):
    """Inserts a new user into the Users table."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Users (name, email, college) VALUES (?, ?, ?)",
        (name, email, college)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"User '{name}' added successfully.")


def view_users():
    """Fetches and prints all users."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("SELECT user_id, name, email, college FROM Users")
    rows = cursor.fetchall()

    print("\n--- Users ---")
    for row in rows:
        print(f"ID: {row.user_id} | Name: {row.name} | Email: {row.email} | College: {row.college}")
    print("-------------\n")

    cursor.close()
    conn.close()


# Quick test
if __name__ == "__main__":
    view_users()