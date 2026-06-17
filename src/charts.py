import matplotlib.pyplot as plt
from analytics import difficulty_distribution, topic_wise_count

def apply_dark_theme(fig, ax):

    # Figure background
    fig.patch.set_facecolor("#1E293B")

    # Plot background
    ax.set_facecolor("#0F172A")

    # Title
    ax.title.set_color("white")

    # Axis labels
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")

    # Tick labels
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    # Spines
    for spine in ax.spines.values():
        spine.set_color("#475569")

    # Grid
    ax.grid(
        axis='y',
        color="#334155",
        linestyle='--',
        alpha=0.6
    )

def create_difficulty_pie_figure(user_id):

    data = difficulty_distribution(user_id)

    fig, ax = plt.subplots(figsize=(7,5))

    fig.patch.set_facecolor("#1E293B")

    if not data:
        ax.text(
            0.5,
            0.5,
            "No data available",
            color="white",
            ha="center",
            va="center"
        )
    else:

        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        colors = [
            "#3B82F6",
            "#06B6D4",
            "#8B5CF6"
        ]

        wedges, texts, autotexts = ax.pie(
            values,
            labels=labels,
            colors=colors,
            autopct='%1.1f%%',
            startangle=90,
            explode=[0.05]*len(values),
            shadow=True
        )

        for text in texts:
            text.set_color("white")

        for text in autotexts:
            text.set_color("white")

        ax.set_title(
            "DSA Problems by Difficulty",
            color="white",
            fontsize=14,
            fontweight="bold"
        )

    return fig


def create_topic_bar_figure(user_id):

    data = topic_wise_count(user_id)

    fig, ax = plt.subplots(figsize=(10,5))

    apply_dark_theme(fig, ax)

    if not data:

        ax.text(
            0.5,
            0.5,
            "No data available",
            color="white",
            ha="center",
            va="center"
        )

    else:

        labels = []
        for row in data:
            topic = row[0]

            if topic == "Dynamic Programming":
                topic = "DP"

            elif topic == "Linked List":
                 topic = "Linked List"

            labels.append(topic)

        values = [row[1] for row in data]
                  
        bars = ax.bar(
            labels,
            values,
            color="#3B82F6",
            edgecolor="#60A5FA",
            linewidth=1.5
        )

        for bar in bars:

            height = bar.get_height()

            ax.annotate(
                str(height),
                xy=(bar.get_x()+bar.get_width()/2, height),
                xytext=(0,5),
                textcoords="offset points",
                ha="center",
                color="white",
                fontsize=9,
                fontweight="bold"
            )

        ax.set_title(
            "Topic-wise DSA Problem Count",
            color="white",
            fontsize=14,
            fontweight="bold"
        )

        ax.set_xlabel("Topic", color="white")
        ax.set_ylabel("Problems Solved")

        ax.tick_params(
        axis='x',
        rotation=45
        )
    fig.tight_layout()

    return fig