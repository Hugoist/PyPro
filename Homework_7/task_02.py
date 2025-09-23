import requests


def download_page(url: str, output_file: str) -> None:
    """
    Download a web page and save its content into a text file
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response.text)

        print(f"Page successfully saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


# Page successfully saved to page.txt
download_page("https://example.com", "page.txt")

# Error: HTTPSConnectionPool(host='olo.lo', port=443):
# Max retries exceeded with url:
# / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x0000017079122FF0>:
# Failed to resolve 'olo.lo' ([Errno 11001] getaddrinfo failed)"))
download_page("https://olo.lo", "ololo.txt")
