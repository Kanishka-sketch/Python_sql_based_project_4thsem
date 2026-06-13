import matplotlib.pyplot as plt
from analytics import difficulty_distribution, topic_wise_count


def show_difficulty_pie_chart(user_id):
    """Displays a pie chart of DSA problems by difficulty."""
    data = difficulty_distribution(user_id)

    if not data:
        print("No data available for difficulty distribution.")
        return

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("DSA Problems by Difficulty")
    plt.show()


def show_topic_bar_chart(user_id):
    """Displays a bar chart of DSA problems by topic."""
    data = topic_wise_count(user_id)

    if not data:
        print("No data available for topic-wise count.")
        return

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color='skyblue')
    plt.xlabel("Topic")
    plt.ylabel("Number of Problems")
    plt.title("Topic-wise DSA Problem Count")
    plt.show()


# Quick test
if __name__ == "__main__":
    show_difficulty_pie_chart(1)
    show_topic_bar_chart(1)