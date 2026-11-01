import sqlite3

DATABASE_NAME = "tv_reviews.db"
RATING_MIN = 1
RATING_MAX = 5

conn = None
cursor = None


def initialize_database():
    """Open the SQLite database and create the episodes table if needed."""
    global conn, cursor

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS episodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            series_name TEXT NOT NULL,
            season INTEGER NOT NULL CHECK (season >= 0),
            episode_number INTEGER NOT NULL CHECK (episode_number > 0),
            episode_name TEXT NOT NULL,
            entertainment INTEGER NOT NULL CHECK (entertainment BETWEEN 1 AND 5),
            drama INTEGER NOT NULL CHECK (drama BETWEEN 1 AND 5),
            iconic INTEGER NOT NULL CHECK (iconic BETWEEN 1 AND 5),
            emotional INTEGER NOT NULL CHECK (emotional BETWEEN 1 AND 5),
            watchable INTEGER NOT NULL CHECK (watchable BETWEEN 1 AND 5),
            rating REAL NOT NULL
        )
    """)
    conn.commit()


def get_non_empty_text(prompt):
    """Ask until the user enters text containing at least one character."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_integer(prompt, minimum=None, maximum=None):
    """Read an integer and optionally enforce inclusive bounds."""
    while True:
        value = input(prompt).strip()
        try:
            number = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if minimum is not None and number < minimum:
            print(f"Please enter a number greater than or equal to {minimum}.")
            continue
        if maximum is not None and number > maximum:
            print(f"Please enter a number no greater than {maximum}.")
            continue
        return number


def calculate_rating(entertainment, drama, iconic, emotional, watchable):
    """Return the average of the five episode category scores."""
    scores = (entertainment, drama, iconic, emotional, watchable)
    if any(not isinstance(score, int) or not RATING_MIN <= score <= RATING_MAX
           for score in scores):
        raise ValueError("Every rating must be a whole number from 1 to 5.")
    return sum(scores) / len(scores)


def add_episode():
    print("\n--- Add Episode ---")

    series = get_non_empty_text("Series name: ")
    season = get_integer("Season (0 or higher): ", minimum=0)
    episode_num = get_integer("Episode number (1 or higher): ", minimum=1)
    episode_name = get_non_empty_text("Episode name: ")

    print(f"\nRate each category from {RATING_MIN} to {RATING_MAX}:")
    entertainment = get_integer("Entertainment value: ", RATING_MIN, RATING_MAX)
    drama = get_integer("Drama value: ", RATING_MIN, RATING_MAX)
    iconic = get_integer("Iconic moments: ", RATING_MIN, RATING_MAX)
    emotional = get_integer("Emotional reaction: ", RATING_MIN, RATING_MAX)
    watchable = get_integer("Watchability: ", RATING_MIN, RATING_MAX)

    rating = calculate_rating(
        entertainment, drama, iconic, emotional, watchable
    )

    cursor.execute("""
        INSERT INTO episodes (
            series_name, season, episode_number, episode_name,
            entertainment, drama, iconic, emotional, watchable, rating
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        series, season, episode_num, episode_name,
        entertainment, drama, iconic, emotional, watchable, rating
    ))

    conn.commit()
    print(f"\nEpisode added! Final rating: {rating:.2f}")


def view_sorted(sort_option):
    """Display episodes using one of the predefined sort options."""
    sort_columns = {
        "rating_desc": "rating DESC",
        "rating_asc": "rating ASC",
        "series": "series_name COLLATE NOCASE ASC, season ASC, episode_number ASC",
        "season": "season ASC, episode_number ASC",
    }

    order_by = sort_columns.get(sort_option)
    if order_by is None:
        print("Invalid sort option.")
        return

    print("\n--- Episodes ---")
    cursor.execute(f"""
        SELECT series_name, season, episode_number, episode_name, rating
        FROM episodes
        ORDER BY {order_by}
    """)
    rows = cursor.fetchall()

    if not rows:
        print("No episodes have been added yet.")
        return

    for series, season, episode_num, episode_name, rating in rows:
        print(
            f"{series} | Season {season} | Ep {episode_num} - "
            f"{episode_name} | Rating: {rating:.2f}"
        )


def main_menu():
    while True:
        print("\n===== TV REVIEW DATABASE =====")
        print("1. Add Episode")
        print("2. View Highest Rated")
        print("3. View Lowest Rated")
        print("4. Sort by Series")
        print("5. Sort by Season")
        print("6. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_episode()
        elif choice == "2":
            view_sorted("rating_desc")
        elif choice == "3":
            view_sorted("rating_asc")
        elif choice == "4":
            view_sorted("series")
        elif choice == "5":
            view_sorted("season")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 6.")


if __name__ == "__main__":
    try:
        initialize_database()
        main_menu()
    except (KeyboardInterrupt, EOFError):
        print("\nApplication closed.")
    finally:
        if conn is not None:
            conn.close()
