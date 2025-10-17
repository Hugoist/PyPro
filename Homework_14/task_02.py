import asyncio
import aiohttp


async def fetch_content(url: str):
    """Downloads the content of a page asynchronously."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    except Exception as e:
        return f"Error fetching {url}: {e}"


async def fetch_all(urls: list):
    """Downloads multiple pages concurrently."""
    tasks = [fetch_content(url) for url in urls]
    results = await asyncio.gather(*tasks)

    for url, content in zip(urls, results):
        print(f"{url} -> {'OK' if 'Error' not in content else content}")


# Example run:
if __name__ == "__main__":
    urls = [
        "https://example.com",
        "https://nonexistent.invalid",
        "https://python.org"
    ]
    asyncio.run(fetch_all(urls))
