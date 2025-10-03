from functions import *

if __name__ == "__main__":
    connection = create_connection("kinobaza.db")
    create_tables(connection)

    while True:
        print("\n")
        print("1. Додати фільм")
        print("2. Додати актора")
        print("3. Показати всі фільми з акторами")
        print("4. Показати унікальні жанри")
        print("5. Показати кількість фільмів за жанром")
        print("6. Показати середній рік народження акторів у фільмах певного жанру")
        print("7. Пошук фільму за назвою")
        print("8. Показати фільми (з пагінацією)")
        print("9. Показати імена всіх акторів та назви всіх фільмів")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

        match choice:
            case "0":
                break

            case "1":
                title = input("Введіть назву фільму: ")
                year = int(input("Введіть рік випуску: "))
                genre = input("Введіть жанр: ")
                print("Доступні актори:")
                actors_list = connection.execute("SELECT * FROM actors").fetchall()
                for actor in actors_list:
                    print(actor[0], actor[1])
                ids = input("Введіть id акторів через кому: ")
                actor_ids = [int(x.strip()) for x in ids.split(",")] if ids else []
                add_movie(connection, title, year, genre, actor_ids)

            case "2":
                name = input("Введіть ім'я актора: ")
                birth_year = int(input("Введіть рік народження: "))
                add_actor(connection, name, birth_year)

            case "3":
                data = get_movies_with_actors(connection)
                print(data)
                for movie, actor in data:
                    print(f"Фільм: {movie}, Акторський склад: {actor}")

            case "4":
                for genre in get_unique_genres(connection):
                    print(genre[0])

            case "5":
                for genre, count in count_movies_by_genre(connection):
                    print(f"{genre}: {count}")

            case "6":
                genre = input("Введіть жанр: ")
                average = avg_birth_year_by_genre(connection, genre)
                print("Середній рік народження акторів:", round(average, 2) if average else "немає даних")

            case "7":
                keyword = input("Введіть ключове слово: ")
                results = search_movies_by_keyword(connection, keyword)
                for r in results:
                    print(r)

            case "8":
                paginate_movies(connection, page_size=3)

            case "9":
                results = get_actors_and_movies(connection)
                for r in results:
                    print(r[0])

    connection.close()
