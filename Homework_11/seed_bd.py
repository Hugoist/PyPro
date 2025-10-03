from functions import create_connection, create_tables, add_actor

actors = [
    ("Кіану Рівз", 1964),
    ("Керрі-Енн Мосс", 1967),
    ("Меттью Макконахі", 1969),
    ("Енн Хетеуей", 1982),
    ("Леонардо Ді Капріо", 1974),
    ("Джозеф Гордон-Левітт", 1981),
    ("Том Генкс", 1956),
    ("Робін Райт", 1966),
    ("Елайджа Вуд", 1981),
]

movies = [
    ("Матриця", 1999, "Наукова фантастика"),
    ("Інтерстеллар", 2014, "Наукова фантастика"),
    ("Початок", 2010, "Наукова фантастика"),
    ("Форрест Гамп", 1994, "Драма"),
    ("Вовк з Уолл-стріт", 2013, "Драма"),
]

movie_cast = [
    # Матриця
    (1, 1),  # Кіану Рівз
    (1, 2),  # Керрі-Енн Мосс

    # Інтерстеллар
    (2, 3),  # Меттью Макконахі
    (2, 4),  # Енн Хетеуей

    # Початок
    (3, 5),  # Леонардо Ді Капріо
    (3, 6),  # Джозеф Гордон-Левітт

    # Форрест Гамп
    (4, 7),  # Том Генкс
    (4, 8),  # Робін Райт

    # Вовк з Уолл-стріт
    (5, 5),  # Леонардо Ді Капріо
]

if __name__ == "__main__":
    connection = create_connection("kinobaza.db")
    cursor = connection.cursor()

    # remove tables before seeding
    cursor.execute("DROP TABLE IF EXISTS movies")
    cursor.execute("DROP TABLE IF EXISTS actors")
    cursor.execute("DROP TABLE IF EXISTS movie_cast")

    create_tables(connection)

    # seed actors
    for name, birth_year in actors:
        add_actor(connection, name, birth_year)

    # seed movies
    for (title, release_year, genre) in movies:
        cursor.execute("""
                       INSERT INTO movies (title, release_year, genre)
                       VALUES (:title, :release_year, :genre)
                       """,
                       {"title": title, "release_year": release_year, "genre": genre}
                       )

    # seed movie_cast
    for movie_id, actor_id in movie_cast:
        cursor.execute("""
                       INSERT INTO movie_cast (movie_id, actor_id)
                       VALUES (:movie_id, :actor_id)
                       """,
                       {"movie_id": movie_id, "actor_id": actor_id})

    connection.commit()
    connection.close()
