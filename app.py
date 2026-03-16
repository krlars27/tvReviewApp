import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("tv_reviews.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS episodes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_name TEXT,
    season INTEGER,
    episode_number INTEGER,
    episode_name TEXT,
    entertainment INTEGER,
    drama INTEGER,
    iconic INTEGER,
    emotional INTEGER,
    watchable INTEGER,
    rating REAL
)
""")

conn.commit()


def calculate_rating(entertainment, drama, iconic, emotional, watchable):
    total = entertainment + drama + iconic + emotional + watchable
    return total / 5.0


def add_episode():
    print("\n--- Add Episode ---")

    series = input("Series name: ")
    season = int(input("Season: "))
    episode_num = int(input("Episode number: "))
    episode_name = input("Episode name: ")

    print("\nRate 1-5:")

    entertainment = int(input("Entertainment value: "))
    drama = int(input("Drama value: "))
    iconic = int(input("Iconic moments: "))
    emotional = int(input("Emotional reaction: "))
    watchable = int(input("Watchable (1-5): "))

    rating = calculate_rating(entertainment, drama, iconic, emotional, watchable)

    cursor.execute("""
    INSERT INTO episodes
    (series_name, season, episode_number, episode_name,
     entertainment, drama, iconic, emotional, watchable, rating)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (series, season, episode_num, episode_name,
          entertainment, drama, iconic, emotional, watchable, rating))

    conn.commit()
    print(f"\nEpisode added! Final Rating: {rating:.2f}")


def view_sorted(order_by):
    print("\n--- Episodes ---")

    cursor.execute(f"""
    SELECT series_name, season, episode_number, episode_name, rating
    FROM episodes
    ORDER BY {order_by}
    """)

    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[0]} | Season {row[1]} | Ep {row[2]} - {row[3]} | Rating: {row[4]:.2f}")


def main_menu():
    while True:
        print("\n===== TV REVIEW DATABASE =====")
        print("1. Add Episode")
        print("2. View Highest Rated")
        print("3. View Lowest Rated")
        print("4. Sort by Series")
        print("5. Sort by Season")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_episode()
        elif choice == "2":
            view_sorted("rating DESC")
        elif choice == "3":
            view_sorted("rating ASC")
        elif choice == "4":
            view_sorted("series_name ASC")
        elif choice == "5":
            view_sorted("season ASC")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


main_menu()
conn.close()
