import requests
import threading
import multiprocessing
import aiohttp
import asyncio
import time

URL = "https://jsonplaceholder.typicode.com/posts/1"
REQUESTS = 500


def fetch_sync(i):
    """Performs HTTP GET synchronously"""
    requests.get(URL)


def run_sync():
    start = time.time()
    for i in range(REQUESTS):
        fetch_sync(i)
    return time.time() - start


def fetch_thread(i):
    """Performs HTTP GET in a thread"""
    requests.get(URL)


def run_threads():
    threads = []
    start = time.time()
    for i in range(REQUESTS):
        t = threading.Thread(target=fetch_thread, args=(i,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return time.time() - start


def fetch_process(i):
    """Performs HTTP GET in a process"""
    requests.get(URL)


def run_processes():
    processes = []
    start = time.time()
    for i in range(REQUESTS):
        p = multiprocessing.Process(target=fetch_process, args=(i,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    return time.time() - start


async def fetch_async(session, i):
    """Performs HTTP GET asynchronously"""
    async with session.get(URL) as response:
        await response.text()


async def run_asyncio():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, i) for i in range(REQUESTS)]
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    approaches = [
        ("Synchronous", run_sync),
        ("Threading", run_threads),
        ("Multiprocessing", run_processes),
        ("AsyncIO", lambda: asyncio.run(run_asyncio()))
    ]

    print(f"{'Approach':<15} {'Time':>10}")
    print("-"*30)
    for name, func in approaches:
        start = time.time()
        func()
        duration = time.time() - start
        print(f"{name:<15} {duration:>10.2f}")
