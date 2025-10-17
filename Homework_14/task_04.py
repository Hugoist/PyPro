import asyncio

async def slow_task(name: str, delay: int):
    """Simulates a long-running task."""
    print(f"{name} started (will take {delay}s)...")
    await asyncio.sleep(delay)
    print(f"{name} finished.")

async def main():
    """Runs several tasks with individual timeouts."""
    tasks = [
        asyncio.wait_for(slow_task("Task 1", 1), timeout=5),
        asyncio.wait_for(slow_task("Task 2", 2), timeout=5),
        asyncio.wait_for(slow_task("Task 3", 6), timeout=5)
    ]

    for i, task in enumerate(asyncio.as_completed(tasks), start=1):
        try:
            await task
        except asyncio.TimeoutError:
            print(f"Task {i} timed out!")

if __name__ == "__main__":
    asyncio.run(main())
