from db_connection import get_connection

def total_problems_solved(user_id):
    """Returns total number of DSA problems solved by the user."""
    conn = get_connection()
    if conn is None:
        return 0

    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) AS TotalSolved FROM DSA_Problems WHERE user_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result.TotalSolved


def difficulty_distribution(user_id):
    """Returns a list of (difficulty, count) tuples."""
    conn = get_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    cursor.execute(
        "SELECT difficulty, COUNT(*) AS Count FROM DSA_Problems "
        "WHERE user_id = ? GROUP BY difficulty",
        (user_id,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [(row.difficulty, row.Count) for row in rows]


def topic_wise_count(user_id):
    """Returns a list of (topic, count) tuples - for bar chart."""
    conn = get_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    cursor.execute(
        "SELECT topic, COUNT(*) AS Count FROM DSA_Problems "
        "WHERE user_id = ? GROUP BY topic",
        (user_id,)
    )
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [(row.topic, row.Count) for row in rows]


def completed_sql_topics(user_id):
    """Returns count of completed SQL practice topics."""
    conn = get_connection()
    if conn is None:
        return 0

    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) AS CompletedTopics FROM SQL_Practice "
        "WHERE user_id = ? AND status = 'Completed'",
        (user_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result.CompletedTopics


def average_mock_score(user_id):
    """Returns average mock interview score."""
    conn = get_connection()
    if conn is None:
        return 0

    cursor = conn.cursor()
    cursor.execute(
        "SELECT AVG(score) AS AverageScore FROM Mock_Interviews WHERE user_id = ?",
        (user_id,)
    )
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result.AverageScore if result.AverageScore is not None else 0


# Quick test
if __name__ == "__main__":
    print("Total problems solved:", total_problems_solved(1))
    print("Difficulty distribution:", difficulty_distribution(1))
    print("Topic-wise count:", topic_wise_count(1))
    print("Completed SQL topics:", completed_sql_topics(1))
    print("Average mock score:", average_mock_score(1))