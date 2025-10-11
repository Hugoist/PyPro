import threading
import requests

# Function to download one file
def download_file(url: str, filename: str) -> None:
    print(f"Завантаження {filename} розпочато")
    response = requests.get(url)
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Завантаження {filename} завершено")

# List of files (URLs) to download
urls = [
    ("https://example.com/file1.jpg", "file1.jpg"),
    ("https://example.com/file2.jpg", "file2.jpg"),
    ("https://example.com/file3.jpg", "file3.jpg"),
]

threads = []

# Create and start threads
for url, name in urls:
    t = threading.Thread(target=download_file, args=(url, name))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print("Усі файли завантажено")
