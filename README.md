# 📺 TV Review App

A Python-based command-line application for tracking television episodes, recording reviews, and comparing episode ratings with a local SQLite database.

## Overview

TV Review App lets users maintain a collection of television episodes and evaluate each episode across five rating categories. The application calculates an overall score from those category ratings and makes it possible to identify the highest- and lowest-rated episodes.

The project demonstrates Python application development, relational database integration, SQL-based data management, and persistent storage.

## Features

- **Add episodes:** Record a series name, season, episode number, and episode title.
- **Rate episodes:** Enter scores across five rating categories.
- **Calculate an overall score:** Average the five category ratings.
- **Persist data:** Store episode information and reviews in an SQLite database.
- **Compare ratings:** Identify highest- and lowest-rated episodes.
- **Retrieve organized results:** View and sort episode information.

## Technologies

| Technology | Purpose |
| --- | --- |
| Python 3 | Application logic |
| SQLite | Local relational database |
| SQL | Data storage and retrieval |

## Getting Started

### Prerequisites

- Python 3
- SQLite support through Python's standard-library `sqlite3` module

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/krlars27/tvReviewApp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd tvReviewApp
   ```

3. Run the application:

   ```bash
   python app.py
   ```

   On systems where Python 3 is invoked separately, use `python3 app.py`.

> **Note:** The commands above assume the application entry point is `app.py`. Adjust the run command if your entry-point filename is different.

## How Ratings Work

Each episode is scored in five individual categories. The application calculates the overall rating as the arithmetic mean of those scores:

```text
Overall rating = (Category 1 + Category 2 + Category 3 + Category 4 + Category 5) / 5
```

## Database

The application uses SQLite for local data persistence. SQLite is accessed through Python's built-in `sqlite3` module, so a separate database server is not required.

The database stores episode details and their associated ratings. The database file is created or used by the application at runtime, depending on its implementation.

## Skills Demonstrated

- Python programming and application logic
- Relational database concepts
- SQLite integration and data persistence
- SQL queries and data retrieval
- Data processing and average calculations
- Command-line application development

## Potential Improvements

- Add the ability to edit and delete episode reviews.
- Add automated unit tests for rating calculations and database operations.
- Provide additional statistics and reporting.
- Build a graphical or web-based interface.
- Separate database access from application logic as the project grows.

## Author

**Kevin Larson**

[GitHub Profile](https://github.com/krlars27)

---

*Personal software development project demonstrating Python programming and relational database management.*
