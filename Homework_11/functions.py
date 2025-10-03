import sqlite3


def create_connection(db_name: str) -> sqlite3.Connection:
    """ create a database connection to the SQLite database"""

    return sqlite3.connect(db_name)


def create_tables(connection: sqlite3.Connection) -> None:
    """ Create the tables movies, actors and movie_cast"""

    cursor = connection.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS movies
                   (
                       id           INTEGER PRIMARY KEY AUTOINCREMENT,
                       title        TEXT    NOT NULL,
                       release_year INTEGER NOT NULL,
                       genre        TEXT    NOT NULL
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS actors
                   (
                       id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       name       TEXT    NOT NULL,
                       birth_year INTEGER NOT NULL
                   )
                   """)

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS movie_cast
                   (
                       movie_id INTEGER,
                       actor_id INTEGER NOT NULL,
                       PRIMARY KEY (movie_id, actor_id),
                       FOREIGN KEY (actor_id) REFERENCES actors (id),
                       FOREIGN KEY (movie_id) REFERENCES movies (id)
                   )
                   """)

    connection.commit()


def add_movie(
        connection: sqlite3.Connection,
        title: str,
        release_year: int,
        genre: str,
        actor_ids: list[int]
) -> None:
    """ Add a movie to the database """

    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO movies (title, release_year, genre)
                   VALUES (:title, :release_year, :genre)
                   """,
                   {"title": title, "release_year": release_year, "genre": genre}
                   )

    movie_id = cursor.lastrowid

    for actor_id in actor_ids:
        cursor.execute("""
                       INSERT INTO movie_cast (movie_id, actor_id)
                       VALUES (:movie_id, :actor_id)
                       """,
                       {"movie_id": movie_id, "actor_id": actor_id})

    connection.commit()


def add_actor(
        connection: sqlite3.Connection,
        name: str,
        birth_year: int,
) -> None:
    """ Add an actor to the database """

    cursor = connection.cursor()
    cursor.execute("""
                   INSERT INTO actors (name, birth_year)
                   VALUES (:name, :birth_year)
                   """,
                   {"name": name, "birth_year": birth_year})
    connection.commit()


def get_movies_with_actors(conn: sqlite3.Connection) -> list[tuple]:
    """Return movies with their actors as comma-separated string"""

    cursor = conn.cursor()
    cursor.execute("""
                   SELECT m.title, GROUP_CONCAT(a.name, ', ') AS actors
                   FROM movies m
                            JOIN movie_cast mc ON m.id = mc.movie_id
                            JOIN actors a ON mc.actor_id = a.id
                   GROUP BY m.id
                   """)
    return cursor.fetchall()


def get_unique_genres(conn: sqlite3.Connection) -> list[tuple]:
    """Return unique movie genres"""

    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT genre FROM movies")
    return cursor.fetchall()


def count_movies_by_genre(conn: sqlite3.Connection) -> list[tuple]:
    """Return number of movies per genre"""

    cursor = conn.cursor()
    cursor.execute("SELECT genre, COUNT(*) FROM movies GROUP BY genre")
    return cursor.fetchall()


def avg_birth_year_by_genre(conn: sqlite3.Connection, genre: str) -> float:
    """Return average birth year of actors in movies of given genre"""

    cursor = conn.cursor()
    cursor.execute("""
                   SELECT AVG(a.birth_year)
                   FROM actors a
                            JOIN movie_cast mc ON a.id = mc.actor_id
                            JOIN movies m ON mc.movie_id = m.id
                   WHERE m.genre LIKE genre
                   """,
                   {"genre_lower_case": genre}
                   )
    return cursor.fetchone()[0]


def search_movies_by_keyword(conn: sqlite3.Connection, keyword: str) -> list[tuple]:
    """Search movies by keyword in title"""

    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM movies WHERE title LIKE :keyword",
        {"keyword": f"%{keyword}%"}
    )
    return cursor.fetchall()


def show_movies_page(conn: sqlite3.Connection, limit: int, offset: int) -> list[str]:
    """Return a list of movie titles for a page"""

    cursor = conn.cursor()
    cursor.execute("""
                   SELECT title
                   FROM movies
                   LIMIT :limit OFFSET :offset
                   """,
                   {"limit": limit, "offset": offset}
                   )
    return [row[0] for row in cursor.fetchall()]


def paginate_movies(conn: sqlite3.Connection, page_size: int) -> None:
    """Interactive pagination of movies"""

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM movies")
    total_movies = cursor.fetchone()[0]
    total_pages = (total_movies + page_size - 1) // page_size
    current_page = 1

    while True:
        offset = (current_page - 1) * page_size
        movies = show_movies_page(conn, page_size, offset)

        print(f"\nСторінка {current_page} з {total_pages} сторінок:")
        for idx, title in enumerate(movies, start=1 + offset):
            print(f"{idx}. {title}")

        command = input("\nnext - наступна сторінка, prev - попередня, :q! - вихід: ").lower()
        if command == "next":
            if current_page < total_pages:
                current_page += 1
            else:
                print("Це остання сторінка")
        elif command == "prev":
            if current_page > 1:
                current_page -= 1
            else:
                print("Це перша сторінка")
        elif command == ":q!":
            break
        else:
            print("Невірна команда")


def get_actors_and_movies(conn: sqlite3.Connection) -> list[tuple]:
    """Return all actor names and movie titles in one list"""

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM actors UNION SELECT title FROM movies")
    return cursor.fetchall()
