import threading


# Function to search for a text in a file
def search_in_file(filename: str, text: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            if text in line:
                print(f"{filename}: рядок {i} містить '{text}'")


if __name__ == "__main__":
    files = ["file1.txt", "file2.txt"]
    search_text = "ololo"

    threads = []
    for file in files:
        t = threading.Thread(target=search_in_file, args=(file, search_text))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Пошук завершено")
