import asyncio
import aiohttp


async def download_image(url: str, filename: str):
    """Downloads an image from a URL and saves it to a file"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as response:
                if response.status == 200:
                    data = await response.read()
                    with open(filename, "wb") as f:
                        f.write(data)
                    print(f"{filename} saved successfully")
                else:
                    print(f"Failed to download {url}: status {response.status}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


async def main():
    """Creates tasks for multiple image downloads and runs them concurrently"""
    images = [
        ("https://www.python.org/static/img/python-logo.png", "python-logo.png"),
        ("https://uk.wikipedia.org/static/images/icons/wikipedia.png", "wikipedia-logo.png"),
    ]

    tasks = [download_image(url, filename) for url, filename in images]

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
