from db_connection import get_connection

def add_company(user_id, company_name, status, notes):
    """Inserts a new company preparation record."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Companies (user_id, company_name, status, notes) "
        "VALUES (?, ?, ?, ?)",
        (user_id, company_name, status, notes)
    )
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Company '{company_name}' added successfully.")


def update_company_status(company_id, new_status):
    """Updates the status of a company preparation record."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Companies SET status = ? WHERE company_id = ?",
        (new_status, company_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No company found with ID {company_id}.")
    else:
        print(f"Company ID {company_id} status updated to '{new_status}'.")

    cursor.close()
    conn.close()


def view_companies(user_id):
    """Fetches and prints all company prep records for a given user."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute(
        "SELECT company_id, company_name, status, notes "
        "FROM Companies WHERE user_id = ? ORDER BY company_id",
        (user_id,)
    )
    rows = cursor.fetchall()

    print("\n--- Company Preparation ---")
    for row in rows:
        print(f"ID: {row.company_id} | {row.company_name} | {row.status} | {row.notes}")
    print("----------------------------\n")

    cursor.close()
    conn.close()

def delete_company(company_id):
    """Deletes a company record by its ID."""
    conn = get_connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("DELETE FROM Companies WHERE company_id = ?", (company_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print(f"No company found with ID {company_id}.")
    else:
        print(f"Company ID {company_id} deleted successfully.")

    cursor.close()
    conn.close()

# Quick test
if __name__ == "__main__":
    view_companies(1)