# TV Review App

A Python command-line application for cataloging television episodes, rating each episode across five categories, and comparing results using a local SQLite database.

## Overview

TV Review App lets users record television episodes and evaluate them with a consistent scoring system. Each episode receives five integer scores, and the application calculates an overall rating as their arithmetic mean.

The project demonstrates Python application logic, relational data storage, SQL queries, and SQLite integration.

## Features

- Add episodes with series, season, episode number, and title.
- Rate episodes on entertainment, drama, iconic moments, emotional reaction, and watchability.
- Calculate an overall score from the five category ratings.
- Persist episode records in SQLite.
- View highest- and lowest-rated episodes.
- Sort episodes by series name or season.

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python 3 | Application logic and command-line interface |
| SQLite | Local relational database |
| SQL | Table creation, inserts, and ordered queries |
| Python `sqlite3` | Database connections and transactions |

## Getting Started

### Prerequisites

- Python 3
- No third-party packages required; `sqlite3` is included with Python.

### Run locally

1. Clone the repository:

   ```bash
   git clone https://github.com/krlars27/tvReviewApp.git
   cd tvReviewApp
   ```

2. Run the application:

   ```bash
   python app.py
   ```

   Use `python3 app.py` if that is the Python command on your system.

The application creates `tv_reviews.db` if it does not already exist and creates the `episodes` table at startup.

## Using the Application

Choose an option from the command-line menu:

| Option | Action |
| --- | --- |
| 1 | Add an episode and enter five category scores |
| 2 | Display episodes from highest to lowest rating |
| 3 | Display episodes from lowest to highest rating |
| 4 | Sort episodes by series name |
| 5 | Sort episodes by season |
| 6 | Exit |

Each category is intended to be scored from 1 to 5. The overall score is:

```text
(Entertainment + Drama + Iconic + Emotional + Watchability) / 5
```

## Database Design

The application creates an `episodes` table with the following fields:

| Column | Type | Description |
| --- | --- | --- |
| `id` | INTEGER | Auto-incrementing primary key |
| `series_name` | TEXT | Television series title |
| `season` | INTEGER | Season number |
| `episode_number` | INTEGER | Episode number |
| `episode_name` | TEXT | Episode title |
| `entertainment` | INTEGER | Entertainment score |
| `drama` | INTEGER | Drama score |
| `iconic` | INTEGER | Iconic moments score |
| `emotional` | INTEGER | Emotional reaction score |
| `watchable` | INTEGER | Watchability score |
| `rating` | REAL | Average of the five category scores |

Episode records are inserted using parameterized SQL values. SQLite runs locally, so no separate database server is needed.

## Project Structure

```text
tvReviewApp/
├── app.py          # Command-line interface and SQLite operations
├── tv_reviews.db   # SQLite database
└── README.md       # Project documentation
```

## Skills Demonstrated

- Python functions and command-line interaction
- Relational database design and table creation
- SQLite connections, transactions, and persistent storage
- SQL `INSERT`, `SELECT`, and `ORDER BY` queries
- Parameterized SQL statements
- Data processing and average calculations

## Potential Improvements

- Validate input and enforce the 1–5 rating range.
- Add options to edit and delete episode records.
- Add search and filtering by series.
- Create automated tests for rating calculations and database operations.
- Separate database access from command-line interface logic.

## Author

**Kevin Larson** · [GitHub Profile](https://github.com/krlars27)

---

*A Python and SQLite project focused on relational data management and practical SQL operations.*
