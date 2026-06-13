import pyodbc

def get_connection():
    """
    Creates and returns a connection to the InterviewTracker database
    using Windows Authentication.
    """
    try:
        connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost\\SQLEXPRESS;'
            'DATABASE=InterviewTracker;'
            'Trusted_Connection=yes;'
        )
        return connection
    except pyodbc.Error as e:
        print("Error connecting to database:", e)
        return None


# Quick test - run this file directly to check connection
if __name__ == "__main__":
    conn = get_connection()
    if conn:
        print("✅ Connection successful!")
        conn.close()
    else:
        print("❌ Connection failed.")