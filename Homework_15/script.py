import csv
import requests
from bs4 import BeautifulSoup


def get_page(url: str) -> None | BeautifulSoup:
    """Download HTML and return BeautifulSoup object"""

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.RequestException as e:
        print(f"Не вдалося завантажити сторінку {url}: {e}")
        return None


def parse_news(soup_obj: BeautifulSoup) -> list[dict | None]:
    """Extract news data from HTML page"""

    news_list = []

    try:
        for item in soup_obj.select("div.article_news_list"):
            title_tag = item.select_one("div.article_title")
            link_tag = item.select_one("div.article_title > a")
            time_tag = item.select_one("div.article_time")

            title = title_tag.get_text(strip=True, separator=" | ") if title_tag else ""
            link = link_tag.get("href") if link_tag else ""
            time = time_tag.get_text(strip=True) if time_tag else ""

            if title and link and time:
                news_list.append({
                    "title": title,
                    "link": link,
                    "time": time,
                })
    except Exception as e:
        print(f"Помилка обробки: {e}")

    return news_list


def save_to_csv(data: list[dict | None], filename: str):
    """Save data to CSV file"""

    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "link", "time"])
        writer.writeheader()
        writer.writerows(data)
    print(f"{len(data)} новин збережено до {filename}")


if __name__ == "__main__":
    url = "https://www.pravda.com.ua/news/"
    soup_obj = get_page(url)

    if soup_obj:
        data = parse_news(soup_obj)
        save_to_csv(data, 'news.csv')
