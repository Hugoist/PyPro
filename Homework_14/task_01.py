import asyncio
import random


async def download_page(url: str):
    """Simulates downloading a web page asynchronously"""
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"{url} завантажено за {delay} с")


async def main(urls: list):
    """Runs multiple asynchronous downloads in parallel"""
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://google.com",
        "https://openai.com",
        "https://github.com"
    ]
    asyncio.run(main(urls))
